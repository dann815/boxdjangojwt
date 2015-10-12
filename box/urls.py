from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^oauth$', views.OAuth, name='oAuth'),
    url(r'^deleteAll$', views.deleteAll, name='deleteAll'),
]