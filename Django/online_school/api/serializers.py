from rest_framework import serializers
from main.models import Student, Teacher, Group
#
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField()


class ItemNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class StudentSerializer(serializers.ModelSerializer):

    group = ItemNameSerializer(read_only=True)
    group_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):

    group = ItemNameSerializer(read_only=True)
    group_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Teacher
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):

    course = ItemNameSerializer(read_only=True)
    course_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Group
        fields = "__all__"