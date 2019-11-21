from django.shortcuts import render

from allauth.account.signals import user_signed_up, email_confirmed
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress

@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):
    user.is_active = False
    user.is_staff = True
    Group.objects.get(name='SurveyManager').user_set.add(user)

    user.save()

@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    new_email_address = EmailAddress.objects.get(email=email_address)
    user = User.objects.get(new_email_address.user)
    user.is_active = True
    user.save()