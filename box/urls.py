from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^users/deleteAll$', views.deleteAll, name='deleteAll'),
    url(r'^new/(?P<new_user_name>\w{0,50})$', views.createUser, name='createUser'),
]