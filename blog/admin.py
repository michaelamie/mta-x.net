from django.contrib import admin
from .models import Entry, Tag, Link

class EntryAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'date', 'markdown', 'published')
  prepopulated_fields = {'slug': ('title',)}
  fields_dict = {
    'fields': (('title', 'published'), 'markdown', 'date', 'tags', 'slug')
  }
  fieldsets = ((None, fields_dict),)

class TagAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug')
  prepopulated_fields = {'slug': ('name',)}

class LinkAdmin(admin.ModelAdmin):
  list_display = ('name', 'url')
  
admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Link, LinkAdmin)