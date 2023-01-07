from django.core.management import BaseCommand
# from main.models import Course, CourseCategory
# import random
# import string
from main.models import ExchangeRate, Bank, Сurrency
from main.parse import parse_exchange



class Command(BaseCommand):

    def handle(self, *args, **options):
        rates_list = parse_exchange()
        bank = Bank.objects
        currency = Сurrency.objects
        for rate in rates_list:
            rate = ExchangeRate.objects.create(
                bank=bank.get(name__exact=rate['bank']),
                currency=currency.get(name__exact=rate['currency']),
                buying=rate["buying"],
                selling=rate["selling"],
                set_course=rate["set_course"],
            )




