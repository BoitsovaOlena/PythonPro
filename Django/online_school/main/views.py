from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, FormView, CreateView
from main.forms import CourseCreateForm, StudentCreateForm
from main.models import CourseCategory, Course
from django.http import Http404
from django.shortcuts import get_object_or_404


class IndexView(ListView):
    template_name = 'index.html'
    model = Course
    paginate_by = 10

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        return queryset.prefetch_related(
            'teacher'
        )

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
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
        context['category_choice'] = get_object_or_404(CourseCategory, id=id)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        return context


class CourseView(TemplateView):
    template_name = 'course.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CourseView, self).get_context_data(*args, **kwargs)
        context.update({
                'course': get_object_or_404(Course, id=context['id'])
            })
        return context


class AddStudentView(FormView):
    template_name = 'add_student.html'
    form_class = StudentCreateForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(AddStudentView, self).form_valid(form)


class AddCourseView(CreateView):
    template_name = 'add_course.html'
    form_class = CourseCreateForm
    success_url = '/'
