# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from Internal.models import Places
# Create your models here.


class DeviceType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Device(models.Model):
    YEAR_CHOICES = []
    for r in range(2005, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    PC_CHOICES = (('New', _('New')), ('Used', _('Used')))
    phone_regex = RegexValidator(regex=r'^\+?1?(\d|-){1,200}$',
                                 message="Invalid Phone Number")
    type = models.ForeignKey(DeviceType, null=True)
    name = models.CharField(max_length=255, blank=True)
    model = models.CharField(max_length=255, blank=True)
    identifier = models.CharField(max_length=255, blank=True)
    serial_number = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(_('year'),
                               choices=YEAR_CHOICES,
                               default=datetime.datetime.now().year)
    specs = models.TextField(blank=True)
    vendor_name = models.CharField(max_length=255, blank=True)
    purchase_date = models.DateField(default=datetime.date.today)
    purchase_condition = models.CharField(max_length=4,
                                          choices=PC_CHOICES, default='New')
    inchs = models.IntegerField(blank=True, null=True)
    sim_number = models.CharField(validators=[phone_regex],
                                  blank=True, max_length=2000,
                                  default=None)
    whose_name = models.ForeignKey(User, null=True, default=None,
                                   related_name="named_device")

    def __str__(self):
        return "%s (%s)" % (self.name, self.identifier)


class DeviceAssingment(models.Model):
    device = models.OneToOneField(Device, related_name="assigned", default=None)
    assign_to = models.ForeignKey(User, null=True, default=None,
                                  related_name="assigned_devices")
    possess_by = models.ForeignKey(User, null=True, default=None,
                                   related_name="possessed_devices")
    possess_place = models.ForeignKey(Places, null=True, default=None,
                                      related_name="possessed_devices")
    issue_date = models.DateField(default=datetime.date.today)
