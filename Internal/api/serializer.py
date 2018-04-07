from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from Internal.models import EmployeeProfile, ProjectHours, Projects


class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = ('avatar', 'gender', 'birth_date', 'location')


class UserSerializer(serializers.ModelSerializer):
    profile = EmployeeProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        read_only_field = ('id', 'email', 'username')


class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(UserFilteredPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(team=request.user)


class ProjectHoursSerializer(serializers.ModelSerializer):

    project = UserFilteredPrimaryKeyRelatedField(queryset=Projects.objects.all())

    class Meta:
        model = ProjectHours
        fields = ('project', 'from_date',  'to_date', 'hours')
        read_only_field = 'employee'

    def to_representation(self, obj):
        response = super(ProjectHoursSerializer, self).to_representation(obj)
        response['project'] = obj.project.name
        return response

    def create(self, validated_data):
        validated_data.update({"employee": self.context['request'].user})
        project = validated_data.get('project')
        if project not in self.context['request'].user.projects_set.all():
            raise exceptions.PermissionDenied()
        ph = super(ProjectHoursSerializer, self).create(validated_data)
        return ph
