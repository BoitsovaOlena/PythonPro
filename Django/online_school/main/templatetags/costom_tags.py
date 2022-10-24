from django import template
from main.models import Course, Student


register = template.Library()


@register.filter
def get_even_numbers(my_list: list) -> list:
    if not isinstance(my_list, list):
        raise TypeError
    numbers_list = []
    for item in my_list:
        if isinstance(item, int) and item % 2 == 0:
            numbers_list.append(item)
    print('Парні числа', numbers_list)
    return numbers_list


@register.filter
def words_count(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError
    words_list = text.split()
    return len(words_list)


@register.inclusion_tag('includes/course_card.html')
def popular_courses(num: int = 5) -> dict:
    students = Student.objects.all().select_related('group')
    courses = {}
    for student in students:
        if courses.get(student.group.course_id):
            my_list = courses[student.group.course_id] + 1
            courses.update({student.group.course_id: my_list})
        else:
            courses.update({student.group.course_id: 1})
    sorted_courses = dict(sorted(courses.items(), key=lambda item: item[1], reverse=True)[:num])
    return {
        'course_list': Course.objects.filter(id__in=sorted_courses.keys())
    }





