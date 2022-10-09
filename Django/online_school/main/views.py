from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from main.models import CourseCategory, Course
from django.http import Http404


class IndexView(ListView):
    template_name = 'index.html'
    model = Course
    paginate_by = 10

# Models, HW_1
    # @staticmethod
    # def queryset_to_str(queryset):
    #     return ', '.join([str(item) for item in queryset])
    #
    # def get_context_data(self, **kwargs):
    #     students = Student.objects.all()
    #     print('\033[0;34mВсі студенти:\033[0m', self.queryset_to_str(students))
    #     groups = Group.objects.all()
    #     print('\033[0;34mВсі групи:\033[0m', self.queryset_to_str(groups))
    #     teachers = Teacher.objects.all()
    #     print('\033[0;34mВсі вчителі:\033[0m', self.queryset_to_str(teachers))
    #     students_in_group = Student.objects.filter(group__name__exact="Java")
    #     print('\033[0;34mВсі студенти в групі Java:\033[0m', self.queryset_to_str(students_in_group))
    #     teacher_group = Teacher.objects.get(name__contains="Оксана Тодоренко").group_id
    #     students_by_teacher = Student.objects.filter(group__exact=teacher_group)
    #     print('\033[0;34mВсі студенти для викладача Оксана Тодоренко:\033[0m', self.queryset_to_str(students_by_teacher))
    #     adult_students = Student.objects.filter(age__gt=20)
    #     print('\033[0;34mВсі студенти старше 20 років:\033[0m', self.queryset_to_str(adult_students))
    #     adults_by_teacher = Student.objects.filter(group__exact=teacher_group, age__gt=20)
    #     print('\033[0;34mВсі студенти старше 20 років для викладача Оксана Тодоренко:\033[0m',
    #           self.queryset_to_str(adults_by_teacher))
    #     students_by_email = Student.objects.filter(email__contains='gmail.com')
    #     print('\033[0;34mВсі студенти  у яких email на домені gmail.com:\033[0m',
    #           self.queryset_to_str(students_by_email))
    #     return {}
    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        return queryset.prefetch_related(
            'teacher'
        )

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['categories'] = CourseCategory.objects.all()
        return context


class CategoryView(ListView):
    template_name = 'index.html'
    model = Course
    paginate_by = 4

    def get(self, request, id):
        self.object_list = super(CategoryView, self).get_queryset().prefetch_related('teacher').filter(category=id)
        if not self.object_list:
            raise Http404
        context = self.get_context_data()
        context['category_choice'] = CourseCategory.objects.filter(id=id)[0]
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context['categories'] = CourseCategory.objects.all()
        return context


class CourseView(TemplateView):
    template_name = 'course.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CourseView, self).get_context_data(*args, **kwargs)
        context.update({
                'categories': CourseCategory.objects.all(),
                'course': Course.objects.filter(id=context['id'])[0]
            })
        return context

