from django.db import models
from django.utils import timezone
from django.urls import reverse

def one_day():
    return timezone.now() + timezone.timedelta(days=1)

def one_week():
    return timezone.now() + timezone.timedelta(days=7)

def one_month():
    return timezone.now() + timezone.timedelta(days=30)

class User(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    f_name = models.CharField(max_length=30, null=False)
    l_name = models.CharField(max_length=30, null=False)
    active_state = models.BooleanField(default=True)

    def get_abs_url(self):
        return reverse('list', args=[self.id])

    def __str__(self):
        return f'{self.f_name} {self.l_name}'

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField(default=one_day)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_abs_url(self):
        return reverse(
            'item-update', args=[str(self.assigned_to.id), str(self.id)]
        )
    
    def __str__(self):
        return f'{self.title} due by {self.due_on}'

    class Meta:
        ordering = ["due_on"]