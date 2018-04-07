from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.renderers import HTMLFormRenderer
from Devices.api.serializer import DeviceSerializer
from Internal.api.serializer import ProjectHoursSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

@login_required
def index(request):
    template_name = 'tintashusers/main/index.html'
    renderer = HTMLFormRenderer()
    serializer = DeviceSerializer()
    form_html = renderer.render(serializer.data)
    context = {'dform': form_html}
    return render(request, template_name, context)



@login_required
def userhours(request):
    template_name = 'tintashusers/projects/hours.html'
    renderer = HTMLFormRenderer()
    serializer = ProjectHoursSerializer(context={'request': request})
    form_html = renderer.render(serializer.data)
    context = {'phform': form_html}
    return render(request, template_name, context)
