from django.conf.urls import url
from posts import views

app_name = 'posts'

urlpatterns = [
    #index page
    url(r'^(?:page/(?P<page>\d+)/)?$', views.IndexView.as_view(), name='paginated_posts'),
    url(r'^add', views.add_post, name='add_post'),
    url(r'^edit/(?P<id>\d+)', views.edit_post, name='edit_post'),
    # #/post-slug-here
    url(r'^(?P<slug>[\w-]+)/$', views.ViewPostView.as_view(), name='view_post'),
    url(r'^search', views.search_post, name='search_post'),
]