from django.conf.urls import url, include

from comments import views as comment_views

urlpatterns = [

    url(r'^$', comment_views.comments_list, name='comments_list'),
    url(r'^(?P<cid>\d+)/$', comment_views.comment_detail, name='comment_detail'),
    #url(r'^(?P<cid>\d+)/edit/$', comment_views.CommentEdit.as_view(), name='comment_edit'),
    url(r'^(?P<cid>\d+)/edit/$', comment_views.comment_edit, name='comment_edit'),
    #url(r'^add/$', comment_views.CommentCreate.as_view(), name='comment_add'),
    url(r'^add/$', comment_views.comment_add, name='comment_add'),
]