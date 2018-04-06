# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Places(models.Model):
    place = models.CharField(max_length=255)

    def __str__(self):
        return self.place


class Projects(models.Model):
    project_name = models.CharField(max_length=255, default='')
    project_description = models.CharField(max_length=255)
    # how many users are working on the project
    user_projects = models.ManyToManyField(User, through='UserProjects') 

    def __str__(self):
        return self.project_name


class Departments(models.Model):
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.department


class EmployeeProfile(models.Model):
    """
    User Profile Model
    """
    GENDER_CHOICES = (('m', _('Male')), ('f', _('Female')))
    DESIGNATION_CHOICES = (('de', _('Developer')), ('pm', _('Project Manager')), ('am', _('Accounts Manager')), 
                          ('ad', _('Admin')), ('fc', _('Front Controller')))
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="profile")
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES, blank=True, null=True)
    designation = models.CharField(max_length=2,
                              choices=DESIGNATION_CHOICES, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    department = models.ForeignKey(Departments, null=True, default=None)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.email


class UserProjects(models.Model):
    """
    admin will add projects and roles
    """
    user = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                blank=True, default=True)
    project = models.ForeignKey(Projects,
                                on_delete=models.CASCADE,
                                blank=True, default=True)
    expected_hours = models.IntegerField(default=0)



class UserProjectHours(models.Model):
    """
    To log hours of the employee
    """
    user = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                blank=True, default=True)
    project = models.ForeignKey(Projects,
                                on_delete=models.CASCADE,
                                blank=True, default=True)
    hours = models.IntegerField(default=0)
    from_date = models.DateField(default=datetime.date.today)
    to_date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
