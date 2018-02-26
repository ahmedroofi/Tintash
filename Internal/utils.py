from Internal.models import EmployeeProfile


def create_profile(strategy, details, response, user, *args, **kwargs):
    try:
        employeeprofile = user.profile
    except EmployeeProfile.DoesNotExist:
        employeeprofile = EmployeeProfile.objects.create(user=user)
