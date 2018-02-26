from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.renderers import HTMLFormRenderer
from Devices.api.serializer import *

@login_required
def index(request):
    template_name = 'tintashusers/main/index.html'
    renderer = HTMLFormRenderer()
    serializer = DeviceSerializer()
    form_html = renderer.render(serializer.data)
    context = {'dform': form_html}
    return render(request, template_name, context)
