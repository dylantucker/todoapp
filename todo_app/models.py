from django.db import models
from django.utils import timezone
from django.urls import reverse

def one_day():
    return timezone.now() + timezone.timedelta(days=1)

def one_week():
    return timezone.now() + timezone.timedelta(days=7)

def one_month():
    return timezone.now() + timezone.timedelta(days=30)
