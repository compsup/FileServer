from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
USERS = (
    ("admin", "admin"),
    ("Greg", "Greg"),
)


class Files(models.Model):
    file_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    file = models.FileField(default='')
    public = models.BooleanField(default=False)
    uploaded_by = models.CharField(
        max_length=50, choices=USERS, default='None')

    def __str__(self):
        return '{}'.format(self.file_name)
