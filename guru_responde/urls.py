from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^home/$', views.pergunta, name='pergunta'),
    url(r'^(?P<pergunta_id>[0-9]+)/$', views.detalhe),
    url(r'^nova_pergunta/$', views.nova_pergunta),
]
