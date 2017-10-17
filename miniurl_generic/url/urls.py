from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'mini_url'
urlpatterns = [
    url(r'^$', views.ListRedirection_view.as_view(), name='home'),
    url(r'^mini_url/acces/(?P<code>\d+)/$', views.AccessUrl, name='redirect'),
    url(r'^about/$', views.FAQView.as_view(), name='about'),
    url(r'create_miniurl/$', views.CreateUrlView.as_view(), name="create-miniurl"),
]
