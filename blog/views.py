from django.views.generic import DetailView, TemplateView
from django.views.generic.dates import (ArchiveIndexView, 
  YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView)
from django.views.generic.detail import SingleObjectMixin
from .models import Entry, Tag, Link
from .settings import settings


class BlogView(object):
  def get_context_data(self, **kwargs):
    context = super(BlogView, self).get_context_data(**kwargs)
    context.update(settings)
    return context
    
class EntryListBase(BlogView):
  date_field = 'date'
  queryset = Entry.objects.filter(published=True)
  context_object_name = 'entries'
  template_name = 'blog/entry_list.html'
  paginate_by = 3
  
class EntryIndexView(EntryListBase, ArchiveIndexView):
  pass
  
class EntryYearView(EntryListBase, YearArchiveView):
  make_object_list = True
  
class EntryMonthView(EntryListBase, MonthArchiveView):
  pass
  
class EntryDayView(EntryListBase, DayArchiveView):
  pass
  
class EntryView(BlogView, DateDetailView):
  date_field = 'date'
  queryset = Entry.objects.filter(published=True)
  template_name = 'blog/entry_detail.html'

class EntryForTagView(EntryIndexView, SingleObjectMixin):
  def get_context_data(self, **kwargs):
    context = super(EntryForTagView, self).get_context_data(**kwargs)
    context['tag'] = self.object
    return context
  def get_queryset(self):
    self.object = self.get_object(Tag.objects.all())
    return self.object.entry_set.filter(published=True)

class AboutView(BlogView, TemplateView):
  template_name = 'blog/about.html'