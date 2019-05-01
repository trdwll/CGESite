from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Forum, Topic, Post

from JKWSite.app_settings import *
from JKWSite.utils import get_online_users


class ForumHomeView(View):
    template_name = 'forum/index.html'

    def get(self, request):
        forum_list = Forum.objects.all()

        return render(request, self.template_name, {
            'FORUM_LIST': forum_list,
            'ONLINE_USERS': get_online_users(),
            'ONLINE_USERS_COUNT': get_online_users().count()
        })


# TODO: Change to ListView
class ForumListView(View):
    template_name = 'forum/forum-list.html'

    def get(self, request, forum_slug):

        # TODO: Sort by recent post or if a topic has been created that's newer
        topic_list = Topic.objects.all().filter(forum=Forum.objects.get(slug=forum_slug)).order_by('-date')

        return render(request, self.template_name, {
            'TOPIC_LIST': topic_list
        })


# TODO: Change to ListView
class ForumTopicListView(View):
    template_name = 'forum/forum-topic.html'

    def get(self, request, forum_slug, topic_slug, topic_id):
        topic = get_object_or_404(Topic.objects.filter(slug=topic_slug, id=topic_id))
        posts = Post.objects.all().filter(topic=topic).order_by('-date')
        posts_count = posts.count()

        return render(request, self.template_name, {
            'topic': topic,
            'POSTS': posts,
            'POSTS_COUNT': posts_count,
        })


class PostReplyToTopic(View):
    def post(self, request, forum_slug, topic_slug, topic_id):
        topic = get_object_or_404(Topic.objects.filter(slug=topic_slug, id=topic_id))

        if request.POST.get('content'):
            reply = Post.objects.create(
                author=request.user, 
                topic=topic,
                # TODO: sanitize input/convert to a proper form so we can use form.cleaned_data['content']
                body=request.POST.get('content'), 
            )
        
        return redirect('forum_topic_page', 
            forum_slug=forum_slug, 
            topic_slug=topic_slug, 
            topic_id=topic_id
        )
