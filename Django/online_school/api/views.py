from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import authentication, permissions
from api.serializers import StudentSerializer, TeacherSerializer, GroupSerializer
from main.models import Student, Teacher, Group

#
# class StudentListView(APIView):
#
#     def get(self, request):
#         students = Student.objects.all().select_related('group')
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)


class StudentListView(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all().select_related('group')


class TeacherListView(ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all().select_related('group')


class GroupListView(ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all().select_related('course')


