from django.conf.urls import patterns, url

from core.views import HeatMap


urlpatterns = patterns('',
    url(r'^predict/$', HeatMap.as_view()),
)
