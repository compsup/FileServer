from django.shortcuts import render, redirect
from .models import Files
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import Http404
from .forms import GeeksForm
import datetime
# Create your views here.

# Home page


def index(request):
    return render(request, 'app/index.html')

# File page


@login_required
def files(request):

    latest_file_list = Files.objects.order_by('-pub_date')[:20]
    context = {'latest_file_list': latest_file_list}
    return render(request, 'app/files.html', context)


def files_upload(request):
    context = {}
    form = GeeksForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, 'app/file-upload.html', context)
# User Profiles


@login_required
def user_profile(request, user_name):
    User = get_user_model()
    user_list = User.objects.all()
    try:
        lookup_user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        raise Http404("User does not exist!")
    context = {'lookup_user': lookup_user, 'user_list': user_list}
    return render(request, 'app/user-profile.html', context)


def docs(request):
    return render(request, 'app/docs.html')
