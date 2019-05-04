"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from .forms import NewsletterSubscribeForm, NewsletterUnSubscribeForm
from .models import Subscriber, Newsletter

from CGESite.utils import get_random_string


class NewsletterSubscribeView(View):
    def post(self, request):
        form = NewsletterSubscribeForm(request.POST)

        if form.is_valid():
            subscriber = Subscriber.objects.filter(email=form.cleaned_data['email'])

            if not subscriber.exists():
                token = get_random_string()
            
                subscriber = Subscriber()
                subscriber.email = form.cleaned_data['email']
                subscriber.token = token
                subscriber.save()

                message = 'You successfully subscribed to {} newsletter. You can unsubscribe from it by going to {} and entering your token {}.'.format(settings.SITE_TITLE, settings.NEWSLETTER_UNSUBSCRIBE_LINK, token)

                send_mail(
					'Newsletter Subsciption - ' + settings.SITE_TITLE,
					message,
					settings.NO_REPLY_EMAIL,
					[form.cleaned_data['email']],
					fail_silently=True
				)
        
                return redirect('newsletter_subscribed')

        return redirect('home_page')


class NewsletterUnSubscribeView(View):
    template_name = 'newsletter/unsubscribe.html'

    def get(self, request):
        return render(request, self.template_name, {
            'form': NewsletterUnSubscribeForm()
        })

    def post(self, request):
        form = NewsletterUnSubscribeForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            token = form.cleaned_data['token']

            subscriber = Subscriber.objects.filter(token=token, email=email)
                
            if subscriber.exists():
                subscriber.delete()

                message = 'You successfully unsubscribed from {} newsletter.'.format(settings.SITE_TITLE)

                send_mail(
					'Newsletter Unsubscibed - ' + settings.SITE_TITLE,
					message,
					settings.NO_REPLY_EMAIL,
					[email],
					fail_silently=True
				)

                return redirect('newsletter_unsubscribed')

        return render(request, self.template_name, {
            'form': form,
        })