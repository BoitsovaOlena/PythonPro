from django import forms
from main.models import Group, CourseTheses, Teacher, CourseCategory, Student, Course, validate_age
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def unique_course_name(value):
    course = Course.objects.filter(name__iexact=value)
    if len(course) > 0:
        raise ValidationError(
            _('Курс з такою назвою вже існує.'),
        )


def unique_student_name(value):
    course = Student.objects.filter(name__contains=value)
    if len(course) > 0:
        raise ValidationError(
            _('Студент з таким прізвищем вже існує.'),
        )


def no_spase_name(obj, name):
    name = obj.cleaned_data[name].strip()
    spaces = name.find(' ')
    if spaces > 0:
        raise forms.ValidationError('Ім\'я та прізвище студента не має містити пробелів')
    return name


class StudentCreateForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(validators=[unique_student_name], error_messages={'unique_student_name': 'Please enter your name'})
    age = forms.IntegerField(validators=[validate_age])
    email = forms.EmailField()
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.widgets.Select(attrs={'style': 'min-width:190px'})
        )

    def clean_first_name(self):
        name = no_spase_name(self, 'first_name')
        return name

    def clean_last_name(self):
        name = no_spase_name(self, 'last_name')
        return name

    def add_student(self):
        name = " ".join((self.cleaned_data['first_name'], self.cleaned_data['last_name']))
        student = Student.objects.create(
            name=name,
            age=self.cleaned_data['age'],
            email=self.cleaned_data['email'],
            group=self.cleaned_data['group']
        )
        return student


class CourseCreateForm(forms.Form):
    name = forms.CharField(validators=[unique_course_name])
    description = forms.CharField(
        widget=forms.widgets.Textarea(attrs={'rows': '5', 'cols': '50', 'style': 'resize: none;'})
    )
    image = forms.ImageField()
    course_theses = forms.ModelMultipleChoiceField(
        queryset=CourseTheses.objects.all(),
        widget=forms.widgets.CheckboxSelectMultiple()
    )
    teacher = forms.ModelMultipleChoiceField(
        queryset=Teacher.objects.all(),
        widget=forms.widgets.CheckboxSelectMultiple()
    )
    category = forms.ModelChoiceField(
        queryset=CourseCategory.objects.all(),
        widget=forms.widgets.Select(attrs={'style': 'min-width:190px'})
    )

    def add_course(self):
        course = Course.objects.create(
            name=self.cleaned_data['name'],
            image=self.cleaned_data['image'],
            description=self.cleaned_data['description'],
            category=self.cleaned_data['category']
        )
        course.course_theses.add(*self.cleaned_data['course_theses'])
        course.teacher.add(*self.cleaned_data['teacher'])
        return course
