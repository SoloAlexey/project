from django.conf.urls import url, include

from core import views as core_views

urlpatterns = [

    url(r'^$', core_views.start_page, name='start_page'),
    url(r'^login/$', core_views.login, name='login'),
    url(r'^logout/$', core_views.logout, name='logout'),
    url(r'registration/$', core_views.registration, name='registration'),
]