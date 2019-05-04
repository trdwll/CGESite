"""
Copyright 2019 Film And Music Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.auth.models import User

from forum.models import Forum, Topic, Post

register = template.Library()


@register.filter(name='get_topic_count_by_forum_slug')
def get_topic_count_by_forum_slug(forum_slug):
	return Topic.objects.all().filter(forum=Forum.objects.get(slug=forum_slug)).count()

@register.filter(name='get_latest_topic_by_forum_slug')
def get_latest_topic_by_forum_slug(forum_slug, arg):
	topic = Topic.objects.filter(forum=Forum.objects.get(slug=forum_slug)).order_by('-date')[:1]

	if topic and topic[0] is not None:
		if arg == 'author':
			return topic[0].author
		elif arg == 'title':
			return topic[0].title 
		elif arg == 'date':
			return topic[0].date
		elif arg == 'url':
			return topic[0].get_absolute_url()
		else:
			return topic[0]
			
	return 'No Topics'

@register.filter(name='get_replies_count_by_forum_slug')
def get_replies_count_by_forum_slug(forum_slug):
	forum = Forum.objects.get(slug=forum_slug)
	topics = Topic.objects.all().filter(forum=forum)
	posts = Post.objects.all().filter(topic__in=topics)

	return topics.count() + posts.count()


@register.filter(name='get_latest_post_by_topic_slug')
def get_latest_post_by_topic_slug(topic_slug, arg):
	topic = Topic.objects.get(slug=topic_slug)
	post = Post.objects.filter(topic=topic).order_by('-date')[:1]

	if topic and post and post[0]:
		if arg == 'author':
			return post[0].author
		elif arg == 'title':
			return post[0].title 
		elif arg == 'date':
			return post[0].date
		elif arg == 'url':
			return post[0].get_absolute_url()
		else:
			return post[0]
			
	return 'No Posts'


@register.filter(name='get_author_post_count_by_topic_author')
def get_author_post_count_by_topic_author(author_name):
	user = User.objects.get(username=author_name)
	return Post.objects.all().filter(author=user).count() + Topic.objects.all().filter(author=user).count()


@register.filter(name='get_author_rank_by_author_name')
def get_author_rank_by_author_name(author):
	author = User.objects.get(username=author)
	
	if author.is_staff or author.is_superuser:
		return 'Staff'
	else:
		return 'Member'


@register.filter(name='get_replies_count_by_topic_slug')
def get_replies_count_by_topic_slug(topic_slug):
	posts_count = Post.objects.all().filter(topic=Topic.objects.get(slug=topic_slug)).count()

	return posts_count + 1