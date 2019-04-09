"""
Copyright 2019 Film And Music Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q

from .models import HomeData
from blog.models import Post


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
		return render(request, self.template_name)


def handler404(request, exception, template_name='error_pages/404.html'):
	return render(request, 'error_pages/404.html', {}, status=404)

def handler500(request, exception, template_name='error_pages/500.html'):
	return render(request, 'error_pages/500.html', {}, status=500)