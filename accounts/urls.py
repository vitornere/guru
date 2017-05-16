from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views

# from wagtail.wagtailadmin import urls as wagtailadmin_urls
# from wagtail.wagtailcore import urls as wagtail_urls
# from wagtail.wagtaildocs import urls as wagtaildocs_urls

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^logout/$', views.logout, name='logout'),
]
