from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Files
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def index(request):

    latest_file_list = Files.objects.order_by('-pub_date')[:20]
    context = {'latest_file_list': latest_file_list}
    return render(request, 'app/index.html', context)
