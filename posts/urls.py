from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add-post', views.add_post, name='add_post')
]