from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
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
                'course': get_object_or_404(Course, id=context['id'])
            })
        return context
