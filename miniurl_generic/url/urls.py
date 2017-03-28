from django.conf.urls import url, include
from django.contrib import admin

from . import views

appname= 'mini_url'
urlpatterns = [
    url(r'^form/$', views.url_view, name='url_field'),
    url(r'^all_url/$', views.ListRedirection_view.as_view(), name='all_url'),
    url(r'^redirect/(?P<code>\d+)/$', views.redirected_view , name='redirect'),
    url(r'^acces/(?P<code>\d+)/$', views.access_url , name='redirect'),
    url(r'^faq/$', views.FAQView.as_view(), name='faq'),
    url(r'^detail/(?P<pk>\d+)/$', views.DetailUrl.as_view() , name='detail'),
    url(r'^create_miniurl$', views.CreateUrlView.as_view(), name="create-miniurl")
]
