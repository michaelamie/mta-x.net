from django.conf.urls import patterns, include, url
from .views import (EntryIndexView, EntryYearView, EntryMonthView,
  EntryDayView, EntryView, EntryForTagView, AboutView)

urlpatterns = patterns('',
  url(r'^$',
    EntryIndexView.as_view(), name='entry-index-view'),
  url(r'^(?P<year>\d{4})/$',
    EntryYearView.as_view(), name='entry-year-view'),
  url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 
    EntryMonthView.as_view(), name='entry-month-view'),
  url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$',
    EntryDayView.as_view(), name='entry-day-view'),
  url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/(?P<slug>[\w-]+)/$',
    EntryView.as_view(), name='entry-view'),
  url(r'^tag/(?P<slug>[\w-]+)/$',
    EntryForTagView.as_view(), name='entry-for-tag-view'),
  url(r'^about/$', 
    AboutView.as_view(), name='about-view'),
)