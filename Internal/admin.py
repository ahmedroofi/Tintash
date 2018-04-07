# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from Internal.models import EmployeeProfile, Projects, ProjectHours

# Register your models here.


class ProfileInline(admin.StackedInline):
    """
    Inline UserProfile model for User
    """
    model = EmployeeProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class UserAdmin(DjangoUserAdmin):
    """
    Register/Display User Model to Django Admin
    """
    inlines = (ProfileInline, )
    ordering = ('email',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ProjectHoursAdmin(admin.ModelAdmin):
    list_display = ('employee', 'project', 'from_date', 'to_date', 'hours',
                    'approved_pm', 'approved_am')
    search_fields = ('employee__username', 'employee__email',
                     'employee__first_name', 'employee__last_name',
                     'project__name')
    list_filter = ('from_date', 'to_date', 'hours',
                   'approved_pm', 'approved_am')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(ProjectHours, ProjectHoursAdmin)
