# import form class from django
from django import forms

# import Files from models.py
from .models import Files


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = "__all__"
