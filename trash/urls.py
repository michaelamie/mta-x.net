from django.conf.urls import patterns, include, url
from trash.views import *

urlpatterns = patterns('',
  url(r'^$', trash_view, name='trash')
)