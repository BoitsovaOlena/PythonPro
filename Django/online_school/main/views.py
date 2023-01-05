from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.aggregates import ArrayAgg
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, FormView, CreateView, UpdateView
from main.forms import CourseCreateForm, StudentCreateForm, StudentEditForm, ContactUsForm
from main.models import CourseCategory, Course, Student, Group
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Count, F


@method_decorator(cache_page(60*15, key_prefix="index"), 'get')
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
        # if 'refresh_count' not in self.request.session:
        #     self.request.session['refresh_count'] = 0
        # self.request.session['refresh_count'] += 1
        # context['refresh_count'] =  self.request.session['refresh_count']
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

    def form_valid(self, form):
        form.save()
        form.send_email()
        return super(AddCourseView, self).form_valid(form)


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


@method_decorator(cache_page(60*30, key_prefix="profile"), 'get')
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


@method_decorator(cache_page(60*90, key_prefix="contact_us"), 'get')
class ContactUsView(FormView):
    template_name = 'contact-us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('contact_us')

    def form_valid(self, form):
        form.send_email()
        return super(ContactUsView, self).form_valid(form)
