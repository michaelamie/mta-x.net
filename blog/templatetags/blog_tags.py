from django import template
from django.db.models import Count
from blog.models import Entry, Tag, Link
from datetime import datetime


register = template.Library()


def sidebar_links():
  links = Link.objects.all()
  return {'links': links}

def sidebar_tags():
  tags = Tag.objects.filter(entry__published=True).annotate(count=Count('entry'))
  return {'tags': tags}

def sidebar_archive():
  # Query the db and load rows into a list
  dates = Entry.objects.dates('date', 'day', 'DESC').filter(published=True)
  '''
  This is the monthly post count listing from Mezzanine.
  - Create a list of key / value pairs
  - Create a list of key / value pairs without duplicate dates
  - Add key / value pairs for duplicate date count to the list 
      that doesn't have duplicate dates
  '''
  date_dicts = [{'date': datetime(date.year, date.month, 1)} for date in dates]
  month_dicts = []
  for date_dict in date_dicts:
    if date_dict not in month_dicts:
      month_dicts.append(date_dict)
  for i, date_dict in enumerate(month_dicts):
    month_dicts[i]['count'] = date_dicts.count(date_dict)
  return {'archive_list': month_dicts}


register.inclusion_tag('blog/sidebar_links.html')(sidebar_links)
register.inclusion_tag('blog/sidebar_tags.html')(sidebar_tags)
register.inclusion_tag('blog/sidebar_archive.html')(sidebar_archive)
