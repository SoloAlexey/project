from django.conf.urls import url, include

from questions import views as question_views

urlpatterns = [

    url(r'^$', question_views.questions_list, name='questions_list'),
    url(r'^(?P<qid>\d+)/$', question_views.question_detail, name='question_detail'),
    # url(r'^create/$', question_views.question_create, name='question_create'),
    url(r'^create/$', question_views.QuestionCreate.as_view(), name='question_create'),
    # url(r'^(?P<qid>\d+)/edit/$', question_views.question_edit, name='question_edit'),
    url(r'^(?P<qid>\d+)/edit/$', question_views.QuestionEdit.as_view(), name='question_edit'),
    url(r'^(?P<qid>\d+)/comments/$', question_views.CommentsView.as_view(), name='question_comments'),
]