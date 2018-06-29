from django.conf.urls import url, include

from categories import views as categories_views
from questions import views as question_views

urlpatterns = [

    url(r'^$', categories_views.categories_list, name='categories_list'),
    url(r'^(?P<pk>\d+)/$', categories_views.category_detail, name='category_detail'),
    url(r'^create/$', categories_views.category_create, name='category_create'),
    url(r'^(?P<pk>\d+)/edit/$', categories_views.category_edit, name='category_edit'),

    #url(r'^(?P<pk>\d+)/questions/', include('questions.urls', namespace='questions')),
    #url(r'^(?P<pk>\d+)/questions/$', question_views.questions_list, name='questions_list'),
    #url(r'^(?P<pk>\d+)/questions/(?P<qid>\d+)/$', question_views.question_detail, name='question_detail'),
]