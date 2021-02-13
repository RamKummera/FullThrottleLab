
from rest_framework import serializers
from app1.models import MembersModel


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembersModel
        fields = '__all__'
