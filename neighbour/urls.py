from django.conf.urls import url, include
from neighbour import views

urlpatterns = [
url(r'^$', views.home, name = "home"),
url(r'register/$', views.register, name = 'register'),
url(r'login/$', views.login, name = 'login'),
url(r'business/$', views.business, name = 'business'),
url(r'contact/$', views.contact, name = 'contact'),
url(r'post/$', views.post, name = 'post'),
url(r'neighbourhood/$', views.neighbourhood, name = 'neighbourhood'),
]