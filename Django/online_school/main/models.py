from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_age(value):
    if value < 18 or value > 90:
        raise ValidationError(
            _('Вік особи має бути від 18 до 90 років'),
            params={'value': value},
        )


class Teacher(models.Model):
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField(validators=[validate_age])
    email = models.EmailField(max_length=100, unique=True)
    group = models.ForeignKey("main.Group", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField(validators=[validate_age])
    email = models.EmailField(max_length=100, unique=True)
    group = models.ForeignKey("main.Group", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
