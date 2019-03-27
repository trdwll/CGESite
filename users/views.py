from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    template_name = 'users/register.html'

    def get(self, request):
        # if request.user.is_authenticated:
           # return redirect('home_page')
           
        return render(request, self.template_name)


class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request):
       # if request.user.is_authenticated:
           # return redirect('home_page')

        return render(request, self.template_name)

