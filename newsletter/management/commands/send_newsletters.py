"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 
from django.core.management.base import BaseCommand, CommandError
from newsletter.models import Newsletter, Subscriber
from django.conf import settings
from django.core.mail import send_mass_mail

class Command(BaseCommand):
    help = 'Sends all subscribers an email as a newsletter.'

    def handle(self, *args, **options):
        subscribers = Subscriber.objects.all().values_list('email', flat=True)
        newsletter = Newsletter.objects.order_by('-id')[0]

        subs = []
    
        for s in subscribers:
            subs.append(s)    
            print(subs)        

        msg = (
            ('Newsletter - ' + newsletter.title, newsletter.body, settings.NO_REPLY_EMAIL, subs),
        )
        send_mass_mail(msg)
