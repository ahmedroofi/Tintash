# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request):
    template_name = 'tintashusers/login/login.html'
    return render(request, template_name)


def logout_view(request):
    url = reverse('tintash:login')
    logout(request)
    return HttpResponseRedirect(url)
