import string
import random
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
USERS = (
    ("duncan", "duncan"),
    ("Greg", "Greg"),
)


def generate_random_string(length):
    rand_string = ''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for i in range(length))
    return rand_string


def directory_path(instance, filename):

    # file will be uploaded to media/random_string/<filename>
    return '{0}/{1}'.format(generate_random_string(16), filename)


class Files(models.Model):
    file_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    file = models.FileField(default='', upload_to=directory_path)
    public = models.BooleanField(default=False)
    uploaded_by = models.CharField(
        max_length=50, choices=USERS, default='None')

    def __str__(self):
        return '{}'.format(self.file_name)
