from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from main.models import CourseCategory, Course, Teacher, CourseTheses
from django.http import Http404


class IndexView(ListView):
    template_name = 'index.html'
    model = Course
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['categories'] = CourseCategory.objects.all()
        return context


class CategoryView(ListView):
    template_name = 'index.html'
    model = Course
    paginate_by = 4

    def get(self, request, id):
        self.object_list = super(CategoryView, self).get_queryset().filter(category=id)
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
                'course': Course.objects.prefetch_related('teacher').filter(id=context['id'])[0]
            })
        print(context['course'])

        return context
    #
    # def get(self, request, *args, **kwargs):
    #     context = super(CourseView, self).get_context_data(*args, **kwargs)
    #     context.update({
    #         'categories': CourseCategory.objects.all(),
    #         'course': Course.objects.get(id=context['id'])
    #     })
    #
    #     return self.render_to_response(context)
        # if not self.object_list:
        #     raise Http404
        # context = self.get_context_data()
        # context.update({
        #     'categories': CourseCategory.objects.all(),
        #     'course': Course.objects.all()
        #
        #     # .select_related(
        #     #     'vendor'
        #     # ).prefetch_related(
        #     #     'tags'
        #     # )
        # })



    # def get_context_data(self, **kwargs):
    #     context = super(CourseView, self).get_context_data(**kwargs)
    #     context.update({
    #         'categories': CourseCategory.objects.all(),
    #         'products': Course.objects.all()
    #
    #
    #         # .select_related(
    #         #     'vendor'
    #         # ).prefetch_related(
    #         #     'tags'
    #         # )
    #     })
    #
    #     return context

    # def get_context_data(self, *args,  **kwargs):
    #     context = super(CourseView, self).get_context_data(*args,  **kwargs)
    #     context['categories'] = CourseCategory.objects.all()
    #
    #     print(context['object'].teacher_id)
    #     return context


