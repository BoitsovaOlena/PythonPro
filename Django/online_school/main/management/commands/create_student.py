from django.core.management import BaseCommand
from main.models import Student, Group
import random
from main.management.commands.create_cources import get_name


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('students_number', type=int)

    def handle(self, *args, **options):
        group = Group.objects.get(id__exact='1')
        for number in range(options['students_number']):
            first_name = get_name(6)
            last_name = get_name(8)
            student = Student.objects.create(
                name=" ".join((first_name, last_name)),
                age=random.randint(18, 80),
                email=f'{last_name}.{first_name}@email.com',
                group=group
            )




