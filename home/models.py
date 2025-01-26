# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Services(models.Model):

    #__Services_FIELDS__
    web support = models.TextField(max_length=255, null=True, blank=True)
    salesforce support = models.TextField(max_length=255, null=True, blank=True)

    #__Services_FIELDS__END

    class Meta:
        verbose_name        = _("Services")
        verbose_name_plural = _("Services")


class Accounts(models.Model):

    #__Accounts_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    phone numbers = models.TextField(max_length=255, null=True, blank=True)

    #__Accounts_FIELDS__END

    class Meta:
        verbose_name        = _("Accounts")
        verbose_name_plural = _("Accounts")



#__MODELS__END
