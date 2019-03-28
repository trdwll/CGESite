from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import LoginForm, RegisterForm

class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request):
        # if request.user.is_authenticated:
           # return redirect('home_page')

        return render(request, self.template_name, {'form': LoginForm()})

    def post(self, request):
        # if request.user.is_authenticated:
           # return redirect('home_page')

        form = LoginForm(request.POST)
        if form.is_valid():
            # TODO: allow email authentication
            username_field = form.cleaned_data['username']
            password_field = form.cleaned_data['password']

            # TODO: google recaptcha validation
            if True:
                user_obj = authenticate(username=username_field, password=password_field)
                if user_obj is not None and user_obj.is_active:
                    login(request, user_obj)
                    return redirect('home_page')
                else:
                    messages.error(request, 'This user does not exist, please check the username and password.')
            else:            
                messages.error(request, 'Recaptcha invalid. Please try again.')
        else:
            messages.error(request, 'Something went wrong. Please try again.')

        return render(request, self.template_name, {'form': form})


class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request):
       # if request.user.is_authenticated:
           # return redirect('home_page')

        return render(request, self.template_name, {'form': RegisterForm()})
