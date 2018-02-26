from rest_framework import serializers
from django.contrib.auth.models import User
from Internal.models import EmployeeProfile


class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = ('avatar', 'gender', 'birth_date', 'location')


class UserSerializer(serializers.ModelSerializer):
    profile = EmployeeSerializer(required=False)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        read_only_field = ('id', 'email', 'username')
