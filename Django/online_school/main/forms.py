from django import forms
from main.models import Group, CourseTheses, Teacher, CourseCategory, Student, Course
from django.utils.translation import gettext_lazy as _


def no_spase_name(name):
    spaces = name.find(' ')
    if spaces > 0:
        raise forms.ValidationError(_('Ім\'я та прізвище студента не має містити пробелів'))
    return name


def unique_last_name(name):
    name = Student.objects.filter(name__contains=name)
    if len(name) > 0:
        raise forms.ValidationError(_('Студент з таким прізвищем вже існує.'))
    return name


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'description': forms.widgets.Textarea(attrs={'rows': '5', 'cols': '50', 'style': 'resize: none;'}),
            'course_theses': forms.widgets.CheckboxSelectMultiple(),
            'teacher': forms.widgets.CheckboxSelectMultiple(),
            'category': forms.widgets.Select(attrs={'style': 'min-width:190px'})
        }
        error_messages = {
            'name': {
                'unique': _("Курс з такою назвою вже існує."),
            },
        }


class StudentCreateForm(forms.ModelForm):
    first_name = forms.CharField(validators=[no_spase_name])
    last_name = forms.CharField(validators=[no_spase_name, unique_last_name])

    class Meta:
        model = Student
        exclude = ['name']
        widgets = {
            'group': forms.widgets.Select(attrs={'style': 'min-width:190px'})
        }

    def save(self, *args, **kwargs):
        student = super(StudentCreateForm, self).save(*args, commit=False, **kwargs)
        student.name = " ".join((self.cleaned_data['first_name'], self.cleaned_data['last_name']))
        student.save()
        self.save_m2m()  # only for models with M2M relation
        return student
