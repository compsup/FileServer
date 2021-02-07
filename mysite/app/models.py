import string
import random
import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Used to make random strings.


def generate_random_string(length):
    rand_string = ''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for i in range(length))
    return rand_string

# Func to save a uploaded file to the correct path.


def directory_path(instance, filename):

    # file will be uploaded to media/random_string/<filename>
    # TODO Have seperate file folders for users.
    return '{0}/{1}'.format(generate_random_string(16), filename)

# Model for uploading files.


class Files(models.Model):
    file_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(
        'date published', null=True)
    file = models.FileField(default='', upload_to=directory_path)
    uploaded_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.file_name)

# Add-on to admin user profile.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    about = models.TextField(max_length=1000, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
