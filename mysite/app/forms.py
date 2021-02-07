# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Files

# create a ModelForm


class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Files
        fields = "__all__"
