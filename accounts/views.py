from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from validate_email import validate_email

from .forms import UserRegistrationForm, ProfileForm
from .models import UserProfile

# Create your views here.


# Account Login views
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('project:project')
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return redirect('project:project')
        else:
            context = {'email': username}
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html', context)


# Account Logout views
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')


def signup(request):
    if request.user.is_authenticated:
        return redirect('project:project')

    form = UserRegistrationForm()
    profile_form = ProfileForm()

    if request.method == 'POST':
        form_data = UserRegistrationForm(request.POST)
        profile_form_data = ProfileForm(request.POST)

        if form_data.is_valid() and profile_form_data.is_valid():
            first_name = form_data.cleaned_data['first_name']
            last_name = form_data.cleaned_data['last_name']
            email = form_data.cleaned_data['email']
            username = form_data.cleaned_data['username']
            password = form_data.cleaned_data['password']
            confirm_password = profile_form_data.cleaned_data['confirm_password']
            phone_number = profile_form_data.cleaned_data['phone_number']
            address = profile_form_data.cleaned_data['address']

            context = {
                'data': request.POST,
                'has_error': False
            }

            if not validate_email(email):
                context['msg'] = "Please provide a valid email address"
                context['color'] = 'alert-danger'
                context['has_error'] = True

            if password != confirm_password:
                context['msg'] = "password don't match"
                context['color'] = 'alert-danger'
                context['has_error'] = True

            if User.objects.filter(email=email).exists():
                context['msg'] = "Email address already exists"
                context['color'] = 'alert-danger'
                context['has_error'] = True

            if context['has_error']:
                return render(request, 'signup.html', context)

            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.is_active = True
            user.is_staff = True
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            #  Set default user group
            worker_group = Group.objects.get(name='workers')
            user.groups.add(worker_group)

            try:
                UserProfile.objects.create(user=user, confirm_password='****', phone_number=phone_number,
                                           address=address)
            except Exception as e:
                print(e)
            return redirect('accounts:login')

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'signup.html', context)
