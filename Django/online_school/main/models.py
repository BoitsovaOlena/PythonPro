from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_age(value):
    if value < 18 or value > 90:
        raise ValidationError(
            _('Вік особи має бути від 18 до 90 років'),
            params={'value': value},
        )


def course_upload_path(obj, file):
    print(obj)
    return f'course/{obj.id}/{file}'


class CourseManager(models.Manager):
    def get_queryset(self):
        queryset = super(CourseManager, self).get_queryset()
        return queryset.exclude(teacher=None)


class NameIt(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Person(NameIt):
    age = models.IntegerField(validators=[validate_age])
    email = models.EmailField(max_length=100, unique=True)

    class Meta:
        abstract = True


class Teacher(Person):
    group = models.ForeignKey("main.Group", on_delete=models.SET_NULL, null=True)


class Group(NameIt):
    pass


class Student(Person):
    group = models.ForeignKey("main.Group", on_delete=models.SET_NULL, null=True)


class CourseCategory(NameIt):
    pass


class CourseTheses(NameIt):
    pass


class Course(NameIt):
    description = models.TextField()
    image = models.ImageField(upload_to=course_upload_path)
    course_theses = models.ManyToManyField("main.CourseTheses")
    teacher = models.ManyToManyField("main.Teacher", blank=True)
    category = models.ForeignKey("main.CourseCategory", on_delete=models.SET_NULL, null=True)

    objects = CourseManager()
