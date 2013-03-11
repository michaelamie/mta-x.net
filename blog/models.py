from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime
import markdown2


class Link(models.Model):
  name = models.CharField(max_length=50)
  url = models.URLField(max_length=250)

  def __unicode__(self):
    return self.name


class Tag(models.Model):
  name = models.CharField(max_length=50)
  slug = models.SlugField(max_length=50)

  def __unicode__(self):
    return self.name

  class Meta:
    ordering=['name']
    
  def get_absolute_url(self):
    return reverse('entry-for-tag-view', kwargs={'slug': self.slug})


class Entry(models.Model):
  title = models.CharField(max_length=50)
  slug = models.SlugField(
    max_length=50, unique_for_date='date',
    help_text='Generated from title')
  date = models.DateField(default=datetime.now)
  tags = models.ManyToManyField(Tag, blank=True)
  published = models.BooleanField(default=True)
  content = models.TextField(blank=True)
  markdown = models.TextField()

  def __unicode__(self):
    return self.title    

  class Meta:
    verbose_name_plural = 'entries'
    ordering = ['-date', 'title'] 

  def get_absolute_url(self):
    kwargs = {
      'year': self.date.year,
      'month': self.date.strftime("%b").lower(),
      'day': self.date.day,
      'slug': self.slug      
    }
    return reverse('entry-view', kwargs=kwargs)
  
  def get_date_url(self):
    kwargs = {
      'year': self.date.year,
      'month': self.date.strftime("%b").lower(),
      'day': self.date.day,
    }
    return reverse('entry-day-view', kwargs=kwargs)     
    
  def save(self):
    self.content = markdown2.markdown(self.markdown, safe_mode=False)
    super(Entry, self).save()