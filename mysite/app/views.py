from django.shortcuts import render, redirect
from .models import Files
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import Http404
from .forms import FileUploadForm
from django.http import HttpResponseRedirect
# Create your views here.

# Home page


def index(request):
    return render(request, 'app/index.html')

# File page


@login_required
def files(request):

    latest_file_list = Files.objects.order_by('-pub_date')[:100]
    context = {'latest_file_list': latest_file_list}
    return render(request, 'app/files.html', context)

# File Upload


@login_required
def files_upload(request):
    context = {}

    # check if form data is valid
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/files/upload-success/')
    else:
        form = FileUploadForm()

    context['form'] = form
    return render(request, 'app/file-upload.html', context)


@login_required
def files_upload_success(request):
    return render(request, 'app/upload-success.html')
# User Profiles


@login_required
def user_profile(request, user_name):
    User = get_user_model()
    user_list = User.objects.all()
    try:
        lookup_user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        raise Http404("User does not exist!")
    context = {'lookup_user': lookup_user}
    return render(request, 'app/user-profile.html', context)


def docs(request):
    return render(request, 'app/docs.html')
