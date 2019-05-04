"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 
from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template.defaultfilters import slugify
from django.conf import settings

from .forms import CreateTopicForm, ReplyTopicForm
from .models import Forum, Topic, Post

from CGESite.app_settings import *
from CGESite.utils import get_online_users, google_recaptcha


class ForumHomeView(View):
    template_name = 'forum/index.html'

    def get(self, request):
        forum_list = Forum.objects.all()

        return render(request, self.template_name, {
            'FORUM_LIST': forum_list,
            'ONLINE_USERS': get_online_users(),
            'ONLINE_USERS_COUNT': get_online_users().count()
        })


class ForumListView(ListView):
    model = Forum
    template_name = 'forum/forum-list.html'
    paginate_by = settings.FORUM_LIST_PAGINATION
    context_object_name = 'topics'

    def get_queryset(self, *args, **kwargs):
        return Topic.objects.all().filter(forum=Forum.objects.get(slug=self.kwargs['forum_slug'])).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forum'] = Forum.objects.get(slug=self.kwargs['forum_slug'])
        return context


class ForumTopicListView(ListView):
    model = Topic
    template_name = 'forum/forum-topic.html'
    paginate_by = settings.FORUM_TOPIC_LIST_PAGINATION
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        topic = get_object_or_404(Topic.objects.filter(slug=self.kwargs['topic_slug'], id=self.kwargs['topic_id']))
        return Post.objects.all().filter(topic=topic).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = get_object_or_404(Topic.objects.filter(slug=self.kwargs['topic_slug'], id=self.kwargs['topic_id']))

        context['topic'] = topic
        context['posts_count'] = Post.objects.all().filter(topic=topic).order_by('-date').count()
        context['form'] = ReplyTopicForm()

        return context


class PostReplyToTopic(View):
    def post(self, request, forum_slug, topic_slug, topic_id):
        topic = get_object_or_404(Topic.objects.filter(slug=topic_slug, id=topic_id))

        form = ReplyTopicForm(request.POST)

        if topic and form.is_valid():
            if google_recaptcha(request)['success']:
                reply = Post()
                reply.author = request.user
                reply.topic = topic
                reply.body = form.cleaned_data['content']
                reply.save()

        return redirect('forum_topic_page', 
            forum_slug=forum_slug, 
            topic_slug=topic_slug, 
            topic_id=topic_id
        )


class CreateTopicView(View):
    template_name = 'forum/create-topic.html'

    def get(self, request, forum_slug):
        forum = get_object_or_404(Forum.objects.filter(slug=forum_slug))

        return render(request, self.template_name, {
            'forum': forum,
            'forum_slug': forum_slug,
            'form': CreateTopicForm()
        })

    def post(self, request, forum_slug):
        form = CreateTopicForm(request.POST)

        forum = get_object_or_404(Forum.objects.filter(slug=forum_slug))

        if forum and form.is_valid() and form.data['content']:
            if google_recaptcha(request)['success']:
                topic = Topic()
                topic.forum = forum
                topic.title = form.cleaned_data['title']
                topic.body = form.cleaned_data['content']
                topic.author = request.user
                topic.slug = slugify(form.cleaned_data['title'])
                topic.save()

                return redirect('forum_topic_page', forum_slug=forum_slug, topic_slug=topic.slug, topic_id=topic.pk)
        
        return render(request, self.template_name, {
            'form': form,
            'forum_slug': forum_slug
        })