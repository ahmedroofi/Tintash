# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Places(models.Model):
    place = models.CharField(max_length=255)

    def __str__(self):
        return self.place


class Projects(models.Model):
    project = models.CharField(max_length=255)

    def __str__(self):
        return self.project


class Departments(models.Model):
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.department


class EmployeeProfile(models.Model):
    """
    User Profile Model
    """
    GENDER_CHOICES = (('m', _('Male')), ('f', _('Female')))
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="profile")
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    department = models.ForeignKey(Departments, null=True, default=None)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.email
