from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^(?:page/(?P<page>\d+)/)?$', views.index, name="index"),
    url(r'^add', views.add_post, name='add_post'),
    url(r'^edit/(?P<id>\d+)', views.edit_post, name='edit_post'),
    url(r'^(?P<slug>[\w-]+)/$', views.view_post, name='view_post'),
    url(r'^search', views.search_post, name='search_post')
]