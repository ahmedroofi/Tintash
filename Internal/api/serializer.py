from rest_framework import serializers
from django.contrib.auth.models import User
from Internal.models import EmployeeProfile, Projects, UserProjects, UserProjectHours


class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = ('avatar', 'gender', 'birth_date', 'location', 'designation')


class UserSerializer(serializers.ModelSerializer):
    profile = EmployeeProfileSerializer(required=False)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        read_only_field = ('id', 'email', 'username')


class ProjectsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Projects
		fields = '__all__'


class UserProjectsSerializer(serializers.ModelSerializer):
	projects = ProjectsSerializer(many=True, read_only=True)
	class Meta:
		model = UserProjects
		fields = '__all__'


class UserProjectHoursSerializer(serializers.ModelSerializer):    
	projects = ProjectsSerializer(many=True, read_only=True)	
	# user = UserSerializer(many=True, read_only=True)
	class Meta:
		model = UserProjectHours
		fields = '__all__'
