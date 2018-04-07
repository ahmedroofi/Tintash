from rest_framework import routers
from django.conf.urls import url, include
from Internal.views import login, main
from Internal.api import views

router = routers.DefaultRouter()
router.register(r'projecthours', views.ProjectHoursView)

urlpatterns = [

    url(r'^$', main.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^login/$', login.login_view, name='login'),
    url(r'^logout/$', login.logout_view, name='logout'),
    url(r'^hours/$', main.userhours, name='userhours')
]
