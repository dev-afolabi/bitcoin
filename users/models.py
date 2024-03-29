from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.core.validators import (
    RegexValidator,
    )
from django.db import models
from django.urls import reverse
from django.conf import settings
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _
from django_resized import ResizedImageField

NAME_REGEX = '^[a-zA-Z ]*$'

GENDER_CHOICE = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Prefer not to say", "Prefer not to say"),
    )

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    first_name = models.CharField(
        max_length=256,
        blank=False,
        validators=[
                RegexValidator(
                    regex=NAME_REGEX,
                    message='Name must be Alphabetic',
                    code='invalid_first_name'
                    )
                ]
        )
    last_name = models.CharField(
        max_length=256,
        blank=False,
        validators=[
                RegexValidator(
                    regex=NAME_REGEX,
                    message='Name must be Alphabetic',
                    code='invalid_last_name'
                    )
                ]
        )

    gender = models.CharField(max_length=25, choices=GENDER_CHOICE,help_text="Select gender")
    date_joined = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
        )

    bonus = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
        )

    picture = ResizedImageField(
        size=[128, 128],
        crop=['top','left'], 
        quality=80,
        upload_to="media-root/",
        null=True,
        blank=False,
        )

    is_staff = models.BooleanField(_("is staff"), default=False)
    is_active = models.IntegerField(default = 1, 
                                   blank = True, 
                                    null = True, 
                                    help_text ='1->Active, 0->Inactive',  
                                    choices =( 
                                    (1, 'Active'), (0, 'Inactive') 
                                    ))
    email_confirmed = models.BooleanField(default=False)

    objects = UserManager()

    # USERNAME_FIELD = 'email'  # use email to log in
    USERNAME_FIELD = 'email'  # use email to log in
    REQUIRED_FIELDS = []  # required when user is created

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        fullname = '%s %s' %(self.first_name, self.last_name)
        return fullname.strip()

    def get_short_name(self):
        return self.first_name

    def Save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
            
    def __str__(self):
        return str(self.last_name+' '+self.first_name)
