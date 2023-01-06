import requests
from datetime import datetime
from lxml import etree
from pprint import pprint
from Django.online_school.main.models import ExchangeRate


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


if __name__ == '__main__':
    my_date = datetime.today()

    # MONO_URL = 'https://api.monobank.ua/bank/currency'
    # mono_response = check_request(MONO_URL, 'application/json; charset=utf-8')
    # pprint(mono_response.json())

    # PRIVAT_URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date={}'
    # privat_response = check_request(PRIVAT_URL.format(my_date.strftime("%d.%m.%Y")), 'application/json;charset=UTF-8')
    # print(privat_response.json())

    # VCURSE_URL = 'https://vkurse.dp.ua/course.json'
    # vkurse_response = check_request(VCURSE_URL, 'application/json')
    # print(vkurse_response.json())
    v = ExchangeRate(buying='44.3', selling = '45.4', set_course='sdvmdsjvmsjmv')
    print(v.id)
    #
    # PIRAEUS_URL = 'https://piraeusbank.ua/ua/get-exchange-nbu'
    # piraeus_response = check_request(PIRAEUS_URL, 'application/json')
    # pprint(piraeus_response.json())
    #
    # OSCHAD_URL = 'https://www.oschadbank.ua/currency-rate'
    # oschad_response = check_request(OSCHAD_URL, 'text/html; charset=utf-8')
    # oschad_html = etree.HTML(oschad_response.text)
    # for item in oschad_html.cssselect('tbody .heading-block-currency-rate__table-row'):
    #     currency = item.cssselect('span')[1].text
    #     print('1,==', currency)
    #     buy = item.cssselect('span')[3].text
    #     print('2,==', buy)
    #     sell = item.cssselect('span')[4].text
    #     print('3,==', sell)
    #
