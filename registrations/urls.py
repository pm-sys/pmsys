from django.conf.urls import url

from . import views

app_name = 'registrations'
urlpatterns = [
    # ex: /registrations/
    url(r'^$', views.index, name='index'),
    # ex: /registrations/5/
    url(r'^(?P<patient_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /registrations/5/results/
    url(r'^(?P<patient_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /registrations/5/update/
    url(r'^(?P<patient_id>[0-9]+)/update/$', views.update, name='update'),
]
