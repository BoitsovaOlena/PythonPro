"""online_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from main import views

urlpatterns = [
    path("<int:course_id>/", views.CourseView.as_view(), name='card'),
    path("add/", views.AddCourseView.as_view(), name='add'),
    path("<int:course_id>/edit/", views.EditCourseView.as_view(), name='edit'),
    # path("<int:course_id>/delete", views.DelCourseView.as_view(), name='delete'),
] 

