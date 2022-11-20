from django.urls import path
from api import views
# from rest_framework.authtoken.views import obtain_auth_token
# шлях реєструєьбся так, тому що ViewSet містить більше 1 View
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'students', views.StudentListView)
router.register(r'teachers', views.TeacherListView)
router.register(r'groups', views.GroupListView)

urlpatterns = [
    # path('get-token/', obtain_auth_token, name='get-token')
] + router.urls
