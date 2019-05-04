"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 
from celery import task
from django.core.mail import send_mail
from .models import Order

from django.conf import settings


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order number. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, settings.NO_REPLY_EMAIL, [order.email])
    return mail_sent
