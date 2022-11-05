from django.core.management import BaseCommand
from main.models import Course, CourseCategory
import random
import string

def get_name(num):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(num))

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('courses_number', type=int)

    def handle(self, *args, **options):
        category = CourseCategory.objects.get(id__exact='1')
        for number in range(options['courses_number']):
            course = Course.objects.create(
                name=get_name(4),
                description=get_name(20),
                category=category
            )
            course.course_theses.add(1)
            course.teacher.add(1)



