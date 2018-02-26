from rest_framework import routers
from django.conf.urls import url, include

from Devices.api import views


router = routers.DefaultRouter()
router.register(r'device', views.DeviceView)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
