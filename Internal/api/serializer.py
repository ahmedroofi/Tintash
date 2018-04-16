import base64
from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from Internal.models import EmployeeProfile, ProjectHours, Projects
from django.conf import settings
from django.contrib.auth import get_user_model
from Internal.api import permissions
from rest_framework.serializers import CharField, EmailField
from django.db.models import Q
from django.core.exceptions import ValidationError
from rest_framework_jwt.settings import api_settings


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
        queryset = super(UserFilteredPrimaryKeyRelatedField,
                         self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(team=request.user)


class ProjectHoursSerializer(serializers.ModelSerializer):

    project = UserFilteredPrimaryKeyRelatedField(
        queryset=Projects.objects.all())

    class Meta:
        model = ProjectHours
        fields = ('id', 'project', 'from_date',  'to_date', 'hours',
                  'approved_am', 'approved_pm')
        extra_kwargs = {
            'approved_am': {'read_only': True},
            'approved_pm': {'read_only': True},
        }

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


class ProjectHoursPMSerializer(serializers.ModelSerializer):

    project = UserFilteredPrimaryKeyRelatedField(
        queryset=Projects.objects.all())
    employee = serializers.SerializerMethodField()

    class Meta:
        model = ProjectHours
        fields = ('id', 'project', 'from_date',  'to_date',
                  'hours', 'employee', 'approved_am', 'approved_pm')
        extra_kwargs = {
            'approved_am': {'read_only': True},
            'employee': {'read_only': True},
        }

    def get_employee(self, obj):
        return '{} {}'.format(obj.employee.first_name, obj.employee.last_name)


class LoginSerializer(serializers.ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(label='Email Address', required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('token', 'email', 'password')

        extra_kwargs = {
            "password":
            {
                "write_only": True
            }

        }

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        password = data["password"]
        if not email:
            raise ValidationError("Email must exists")

        user = User.objects.filter(
            Q(email=email)
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Incorrect Email")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials")

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        print(token)
        data["token"] = token
        return data
