import requests
from datetime import datetime
from lxml import etree


def check_request(url, content_type):
    """
    The response to the url request is being checked. If the status of the response is within 200s and the type of
    content corresponds to the one specified in the arguments, the function returns the response. Otherwise None.
    :param url:
    :type url: str
    :param content_type: The value should correspond to the 'Content-Type' from the headers of the response.
    :type content_type: str
    :return: A response received from the server that satisfies our requirements.
    :rtype: requests.models.Response|None
    """
    try:
        resp = requests.get(url)
    except Exception as e:
        print(e)
    else:
        if 300 > resp.status_code >= 200:
            if resp.headers.get('Content-Type') == content_type:
                return resp
        return None

def make_dict(bank, currency, buying, selling, date):
    """
    :return:
    :rtype:dict
    """
    set_course = bank + currency + date
    return {
        "bank": bank,
        "currency": currency,
        "buying": buying,
        "selling": selling,
        "set_course": set_course
    }


def parse_exchange():
    """
    Receives information on exchange rates from 5 sources.
    :return: List of dictionaries with exchange rates.
    :rtype: List
    """
    rates = []
    my_date = datetime.today()

    MONO_URL = 'https://api.monobank.ua/bank/currency'
    mono_response = check_request(MONO_URL, 'application/json; charset=utf-8')
    for item in mono_response.json()[0:9]:
        currencies = {
            '840': 'USD',
            '978': 'EUR',
            '826': 'GBP',
            '392': 'JPY',
            '756': 'CHF',
            '156': 'CNY',
            '784': 'AED',
            '971': 'AFN'
        }
        if item['currencyCodeB'] == 980:
            record = make_dict(
                bank='monobank',
                currency=currencies[str(item['currencyCodeA'])],
                buying=str(item['rateBuy']),
                selling=str(item['rateSell']),
                date=my_date.strftime("%d.%m.%Y")
            )
            rates.append(record)

    PRIVAT_URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date={}'
    privat_response = check_request(PRIVAT_URL.format(my_date.strftime("%d.%m.%Y")), 'application/json;charset=UTF-8')
    for item in privat_response.json()['exchangeRate']:
        if item.get('purchaseRate') and item.get('saleRate'):
            record = make_dict(
                bank='privatbank',
                currency=item['currency'],
                buying=item['purchaseRate'],
                selling=item['saleRate'],
                date=my_date.strftime("%d.%m.%Y")
            )
            rates.append(record)

    VCURSE_URL = 'https://vkurse.dp.ua/course.json'
    vkurse_response = check_request(VCURSE_URL, 'application/json')
    for currency, rate in vkurse_response.json().items():
        currencies = {
            'Dollar': 'USD',
            'Euro': 'EUR',
            'Pln': 'PLN'
        }
        record = make_dict(
            bank='vkurse',
            currency=currencies[currency],
            buying=rate['buy'],
            selling=rate['sale'],
            date=my_date.strftime("%d.%m.%Y")
        )
        rates.append(record)

    PIRAEUS_URL = 'https://piraeusbank.ua/ua/get-exchange-nbu'
    piraeus_response = check_request(PIRAEUS_URL, 'application/json')
    for item in piraeus_response.json()['rates']:
        record = make_dict(
            bank='piraeusbank',
            currency=item['targetCurrency'],
            buying=item['buying'],
            selling=item['selling'],
            date=my_date.strftime("%d.%m.%Y")
        )
        rates.append(record)

    OSCHAD_URL = 'https://www.oschadbank.ua/currency-rate'
    oschad_response = check_request(OSCHAD_URL, 'text/html; charset=utf-8')
    oschad_html = etree.HTML(oschad_response.text)
    for item in oschad_html.cssselect('tbody .heading-block-currency-rate__table-row')[0:7]:
        currency = item.cssselect('span')[1].text
        buy = item.cssselect('span')[3].text
        sell = item.cssselect('span')[4].text
        record = make_dict(
            bank='oschadbank',
            currency=currency,
            buying=buy,
            selling=sell,
            date=my_date.strftime("%d.%m.%Y")
        )
        rates.append(record)
    return rates
