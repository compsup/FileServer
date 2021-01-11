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
    return render(request, 'app/index.html')


@login_required
def files(request):
    latest_file_list = Files.objects.order_by('-pub_date')[:20]
    context = {'latest_file_list': latest_file_list}
    return render(request, 'app/files.html', context)


@login_required
def user_profile(request):
    return render(request, 'app/files.html')
