from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import Teacher, Group, Student


class IndexView(TemplateView):
    template_name = 'index.html'

    @staticmethod
    def queryset_to_str(queryset):
        return ', '.join([str(item) for item in queryset])

    def get_context_data(self, **kwargs):
        students = Student.objects.all()
        print('\033[0;34mВсі студенти:\033[0m', self.queryset_to_str(students))
        groups = Group.objects.all()
        print('\033[0;34mВсі групи:\033[0m', self.queryset_to_str(groups))
        teachers = Teacher.objects.all()
        print('\033[0;34mВсі вчителі:\033[0m', self.queryset_to_str(teachers))
        students_in_group = Student.objects.filter(group__name__exact="Java")
        print('\033[0;34mВсі студенти в групі Java:\033[0m', self.queryset_to_str(students_in_group))
        teacher_group = Teacher.objects.get(name__contains="Оксана Тодоренко").group_id
        students_by_teacher = Student.objects.filter(group__exact=teacher_group)
        print('\033[0;34mВсі студенти для викладача Оксана Тодоренко:\033[0m', self.queryset_to_str(students_by_teacher))
        adult_students = Student.objects.filter(age__gt=20)
        print('\033[0;34mВсі студенти старше 20 років:\033[0m', self.queryset_to_str(adult_students))
        adults_by_teacher = Student.objects.filter(group__exact=teacher_group, age__gt=20)
        print('\033[0;34mВсі студенти старше 20 років для викладача Оксана Тодоренко:\033[0m',
              self.queryset_to_str(adults_by_teacher))
        students_by_email = Student.objects.filter(email__contains='gmail.com')
        print('\033[0;34mВсі студенти  у яких email на домені gmail.com:\033[0m',
              self.queryset_to_str(students_by_email))
        return {}