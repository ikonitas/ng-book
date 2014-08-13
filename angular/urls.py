from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hits/$', views.AngularViewHits.as_view()),
    url(r'^hit/$', views.AngularViewHit.as_view()),
]
