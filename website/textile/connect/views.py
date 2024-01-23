from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, OwnerPublishForm, WorkerProfileForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import OwnerPublish, WorkerProfile
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.db.models import CharField, Value
from django.db.models.functions import Concat


def user_signup(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system #################################### 
			htmly = get_template('Email.html')
			d = { 'username': username }
			subject, from_email, to = 'welcome', 'your_email@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			################################################################## 
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('user_login')
	else:
		form = UserRegisterForm()
	return render(request, 'user_signup.html', {'form': form, 'title':'register here'})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password, auth='connect.backends.CustomUserBackend')

        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            if user.is_owner:
                return redirect('owner_dashboard')
            elif user.is_worker:
                return redirect('worker_dashboard')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user_login.html', {'form':form, 'title':'log in'})

def owner_dashboard(request):
    return render(request, 'owner_dashboard.html')

def worker_dashboard(request):
    return render(request, 'worker_dashboard.html')


def owner_publish_form(request):
    k=0
    # Check if the user is authenticated
    if request.user.is_authenticated:
        user = request.user
        # Check if the user has already submitted a form
        existing_entries = OwnerPublish.objects.filter(owner=user)
        if existing_entries.exists():
            # If there are existing entries, use the first one
            existing_entry = existing_entries.first()
            form = OwnerPublishForm(request.POST or None, instance=existing_entry)
        else:
            # If no existing entries, create a new form
            form = OwnerPublishForm(request.POST or None)

        if request.method == 'POST' and k==0:
            if form.is_valid():
                form.instance.owner = user
                form.save()
                k=1
                return redirect('owner_publish_form')

        return render(request, 'owner_publish_form.html', {'form': form})
    else:
        # Handle the case where the user is not authenticated
        return redirect('user_login')  # Redirect to your login view


def worker_profile(request):
    k=0
    # Check if the user is authenticated
    if request.user.is_authenticated:
        user = request.user

        # Check if the user has already submitted a form
        existing_entries = WorkerProfile.objects.filter(worker=user)
        print(existing_entries)
        if existing_entries.exists():
            # If there are existing entries, use the first one
            existing_entry = existing_entries.first()
            form = WorkerProfileForm(request.POST or None, instance=existing_entry)
        else:
            # If no existing entries, create a new form
            form = WorkerProfileForm(request.POST or None)
        if request.method == 'POST' and k==0:
            if form.is_valid():
                form.instance.worker = request.user
                form.save()
                k=1
                return redirect('worker_profile')
            else:
                print(form.errors)

        return render(request, 'worker_profile.html', {'form': form})
    else:
        # Handle the case where the user is not authenticated
        return redirect('user_login')  # Redirect to your login view

def owner_list(request):
    owners = OwnerPublish.objects.all()
    return render(request, 'owner_list.html', {'owners': owners})

def worker_list(request):
    workers = WorkerProfile.objects.all()
    return render(request, 'worker_list.html', {'workers': workers})


def filtered_workers(request):
    work_locations = request.GET.getlist('work_locations')
    # Apply filters based on selected work locations and area of work

    filtered_workers = WorkerProfile.objects.filter(
        work_location__in=work_locations,
    )

    worker_data = list(filtered_workers.values())
    return JsonResponse(worker_data, safe=False)

def filtered_owners(request):
    industries = request.GET.getlist('industries')
    if industries:
        industries_string = industries[0]
        # Split the string into a list using commas as separators
        industries_list = industries_string.split(',')

    filtered_owners = OwnerPublish.objects.filter(
        industrial_park_name__in=industries_list,
    )
    
    owners_data = list(filtered_owners.values())
    
    return JsonResponse(owners_data, safe=False)

