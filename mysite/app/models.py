import string
import random
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


def generate_random_string(length):
    letters = string.ascii_lowercase
    global rand_string
    rand_string = ''.join(random.choice(letters) for i in range(length))


generate_random_string(16)


class Files(models.Model):
    file_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    file = models.FileField(default='', upload_to=rand_string)
    public = models.BooleanField(default=False)
    uploaded_by = models.CharField(
        max_length=50, choices=USERS, default='None')

    def __str__(self):
        return '{}'.format(self.file_name)
