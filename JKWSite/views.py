"""
Copyright 2019 Film And Music Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

from .models import HomeData
from .forms import ContactForm
from blog.models import Post

from .utils import google_recaptcha


class HomeView(View):
	template_name = 'home-page.html'

	def get(self, request):

		return render(request, self.template_name, {
			'homedata': HomeData.objects.get(),
			'posts': Post.objects.all().order_by('-published_date')[:3]
		})


class ContactView(View):
	template_name = 'contact-page.html'

	def get(self, request):
		return render(request, self.template_name, {
			'form': ContactForm()
		})

	def post(self, request):
		form = ContactForm(request.POST)

		if form.is_valid():
			if google_recaptcha(request)['success']:
				send_mail(
					'Contact Request - ' + form.cleaned_data['title'],
					form.cleaned_data['content'],
					form.cleaned_data['email'],
					[settings.CONTACT_EMAIL],
					fail_silently=True
				)
			
		return redirect('home_page')
