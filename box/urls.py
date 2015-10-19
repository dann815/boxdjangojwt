from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^appusers/deleteAll$', views.deleteAll, name='deleteAll'),
]