from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import CourseCategory, Course


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'categories': CourseCategory.objects.all(),
            'courses': Course.objects.all(),
        })
        return context

