from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^register', views.registration, name='registration'),
    url(r'^login', views.login_user, name='login'),
    url(r'^account', views.account, name='account'),
    url(r'^logout', views.logout_user, name='logout')
]