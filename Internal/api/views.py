from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from Internal.api.permissions import PHOwner
from Internal.api.serializer import ProjectHoursSerializer,\
    ProjectHoursPMSerializer, LoginSerializer
from Internal.models import ProjectHours
from Internal.api.permissions import IsAuthenticatedOrCreate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from social.exceptions import AuthAlreadyAssociated
from rest_framework import viewsets, status, generics
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
import json as simplejson
from django.http import JsonResponse
# authenticate: will check if the user exist
from django.contrib.auth import authenticate
# api_settings: will help generating the token
from rest_framework_jwt.settings import api_settings

from rest_framework.permissions import AllowAny

from .serializer import LoginSerializer


# Create your views here.
class ProjectHoursView(viewsets.ModelViewSet):
    queryset = ProjectHours.objects.all()

    def get_queryset(self, *args, **kwargs):
        return ProjectHours.objects.all().filter(employee=self.request.user)

    def get_serializer_class(self):
        if "PM" in self.request.user.groups.all().\
                values_list('name', flat=True):
            return ProjectHoursPMSerializer
        return ProjectHoursSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return (IsAuthenticated(), PHOwner())
        else:
            return (IsAuthenticated(),)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
