from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from Internal.api.permissions import PHOwner
from Internal.api.serializer import ProjectHoursSerializer
from Internal.models import ProjectHours


# Create your views here.
class ProjectHoursView(viewsets.ModelViewSet):
    serializer_class = ProjectHoursSerializer
    queryset = ProjectHours.objects.all()

    def get_queryset(self, *args, **kwargs):
        return ProjectHours.objects.all().filter(employee=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return (IsAuthenticated(), PHOwner())
        else:
            return (IsAuthenticated(),)
