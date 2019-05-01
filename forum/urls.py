from django.urls import path

from . import views

urlpatterns = [
    path('', views.ForumHomeView.as_view(), name='forum_home_page'),
    path('<slug:forum_slug>/', views.ForumListView.as_view(), name='forum_list_page'),
    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/', views.ForumTopicListView.as_view(), name='forum_topic_page'),

    path('<slug:forum_slug>/<slug:topic_slug>.<int:topic_id>/reply/', views.PostReplyToTopic.as_view(), name='reply_to_topic'),

    # TODO: Add pagination for ForumListView and ForumTopicListView
]