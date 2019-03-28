from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm

class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home_page')

        return render(request, self.template_name, {'form': LoginForm()})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home_page')

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
        #     return redirect('home_page')

        return render(request, self.template_name, {'form': RegisterForm()})

    def post(self, request):
        # if request.user.is_authenticated:
        #     return redirect('home_page')
        form = RegisterForm(request.POST)
		
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            tos_agree = request.POST.get('tos_agree', 'off')

            if True:#google_recaptcha(request)['success']:
                if tos_agree != 'off':

                    # check if the password is in the username
                    if password not in username:

                        # check if the passwords are matching
                        if password == password_confirm:
                            # __iexact checks if the username/email exists in any case
                            db_username = User.objects.filter(username__iexact=username).exists()
                            db_email = User.objects.filter(email__iexact=email).exists()

                            # check if the database contains the username or email before registering the user
                            if not db_username:
                                if not db_email:
                                    user = User.objects.create_user(username=username, email=email, password=password)
                                    user.save()

                                    # TODO: create the user profile - we need to remove this eventually so figure out a way to do that (when create_user is called or something)

                                    if user:
                                        # TODO: look into removing backend as it's ugly lol
                                        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                                        return redirect('home_page')
                                else:
                                    messages.error(request, 'That email already exists for another user. Please try another email.')
                            else:
                                messages.error(request, 'That username already exists for another user. Please use another username.')
                        else:
                            messages.error(request, 'Passwords do not match. Please re-enter the passwords.')
                    else:
                        messages.error(request, 'Password is too similar to your username.')
                else:
                    messages.error(request, 'You did not accept the Terms of Service.')
            else:
                messages.error(request, 'Captcha was invalid. Please try again.')
        else:
            messages.error(request, 'Something went wrong. Please try again.')

        return render(request, self.template_name, {'form': form})