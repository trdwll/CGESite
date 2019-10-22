"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

from .models import HomeData, HomeCarousel, Character
from .forms import ContactForm, SearchForm
from blog.models import Post
from forum.models import Topic
from store.models import Product

from .utils import google_recaptcha


class HomeView(View):
	template_name = 'home-page.html'

	def get(self, request):

		return render(request, self.template_name, {
			'homedata': HomeData.objects.get(),
			'characters': Character.objects.all(),
			'mercenary_characters': Character.objects.filter(character_class='Mercenary'),
			'medic_characters': Character.objects.filter(character_class='Medic'),
			'sniper_characters': Character.objects.filter(character_class='Sniper'),
			'engineer_characters': Character.objects.filter(character_class='Engineer'),
			'carousel': HomeCarousel.objects.all(),
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
					settings.CONTACT_EMAIL,
					form.cleaned_data['email'],
					fail_silently=True
				)
			
		return redirect('home_page')


class SearchResultsView(View):
	template_name = 'search-page.html'

	def get(self, request):
		
		return render(request, self.template_name, {'form': SearchForm()})



	def post(self, request):

		form = SearchForm(request.POST)

		if form.is_valid():
			# if google_recaptcha(request)['success']: # TODO: implement recaptcha at a later date on the actual template and not in the navbar
			s_data = form.cleaned_data['search_input']
			blog_posts = Post.objects.filter(Q(title__icontains=s_data) | Q(body__icontains=s_data))
			forum_topics = Topic.objects.filter(Q(title__icontains=s_data) | Q(body__icontains=s_data))
			store_products = Product.objects.filter(Q(title__icontains=s_data) | Q(description__icontains=s_data) | Q(price__icontains=s_data))

			count = blog_posts.count() + forum_topics.count() + store_products.count()

			data = { 'search_results_count': count, 'blog_posts': blog_posts, 'forum_topics': forum_topics, 'store_products': store_products }
			return render(request, self.template_name, { 'search_data': data, 'form': form })

		print(form)
		return redirect('home_page')