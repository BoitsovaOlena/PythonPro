from django.contrib import admin
from main import models


admin.site.register(models.Student)
admin.site.register(models.Group)
admin.site.register(models.Teacher)
admin.site.register(models.CourseCategory)
admin.site.register(models.CourseTheses)
admin.site.register(models.Course)


