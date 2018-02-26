from django.conf.urls import url
from Internal.views import login, main


urlpatterns = [

    url(r'^$', main.index, name='index'),
    url(r'^login/$', login.login_view, name='login'),
    url(r'^logout/$', login.logout_view, name='logout')


]
