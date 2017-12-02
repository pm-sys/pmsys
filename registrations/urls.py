from django.conf.urls import url

from . import views

app_name = 'registrations'
urlpatterns = [
    # ex: /registrations/
    url(r'^$', views.index, name='index'),
]
