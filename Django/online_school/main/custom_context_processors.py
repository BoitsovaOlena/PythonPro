from main.models import CourseCategory


def get_categories(request):
    return {
        'categories': CourseCategory.objects.all()
    }
