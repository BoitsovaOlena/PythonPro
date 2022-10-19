from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from main.forms import StudentCreateForm, CourseCreateForm
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
        context['category_choice'] = get_object_or_404(CourseCategory, id=id)
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
                'course': get_object_or_404(Course, id=context['id'])
            })
        return context


class AddStudentView(TemplateView):
    template_name = 'add_student.html'

    def get_context_data(self, **kwargs):
        context = super(AddStudentView, self).get_context_data(**kwargs)
        context['categories'] = CourseCategory.objects.all()
        context['form'] = StudentCreateForm()
        return context

    def post(self, request):
        form = StudentCreateForm(data=request.POST)
        if form.is_valid():
            form.add_student()
            return redirect('/')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class AddCourseView(TemplateView):
    template_name = 'add_course.html'

    def get_context_data(self, **kwargs):
        context = super(AddCourseView, self).get_context_data(**kwargs)
        context['categories'] = CourseCategory.objects.all()
        context['form'] = CourseCreateForm()
        return context

    def post(self, request):
        form = CourseCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.add_course()
            return redirect('/')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
