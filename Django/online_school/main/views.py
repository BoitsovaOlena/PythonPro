from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, FormView, CreateView, UpdateView
from main.forms import CourseCreateForm, StudentCreateForm, StudentEditForm
from main.models import CourseCategory, Course, Student, Course
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
                'course': get_object_or_404(Course, id=context['course_id'])
            })
        return context


class StudentsView(ListView):
    template_name = 'students.html'
    model = Student
    paginate_by = 8

    def get_queryset(self):
        queryset = super(StudentsView, self).get_queryset()
        return queryset.select_related('group').order_by('name')


class AddStudentView(FormView):
    template_name = 'add_student.html'
    form_class = StudentCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super(AddStudentView, self).form_valid(form)


class AddCourseView(CreateView):
    template_name = 'add_course.html'
    form_class = CourseCreateForm
    success_url = reverse_lazy('home')


class EditStudentView(UpdateView):
    template_name = 'add_student.html'
    model = Student
    form_class = StudentEditForm
    success_url = reverse_lazy('student:list')
    pk_url_kwarg = 'student_id'

    def get_initial(self):
        name = self.object.name.split()
        return {'first_name': name[0], 'last_name': name[1]}


class EditCourseView(UpdateView):
    template_name = 'add_course.html'
    model = Course
    form_class = CourseCreateForm
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'course_id'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
