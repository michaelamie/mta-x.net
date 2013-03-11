# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Entry.title'
        db.alter_column(u'blog_entry', 'title', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Entry.slug'
        db.alter_column(u'blog_entry', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

        # Changing field 'Tag.slug'
        db.alter_column(u'blog_tag', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

        # Changing field 'Tag.name'
        db.alter_column(u'blog_tag', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Link.url'
        db.alter_column(u'blog_link', 'url', self.gf('django.db.models.fields.URLField')(max_length=250))

        # Changing field 'Link.name'
        db.alter_column(u'blog_link', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'Entry.title'
        db.alter_column(u'blog_entry', 'title', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Entry.slug'
        db.alter_column(u'blog_entry', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=255))

        # Changing field 'Tag.slug'
        db.alter_column(u'blog_tag', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=255))

        # Changing field 'Tag.name'
        db.alter_column(u'blog_tag', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Link.url'
        db.alter_column(u'blog_link', 'url', self.gf('django.db.models.fields.URLField')(max_length=255))

        # Changing field 'Link.name'
        db.alter_column(u'blog_link', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'blog.entry': {
            'Meta': {'ordering': "['-date', 'title']", 'object_name': 'Entry'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'markdown': ('django.db.models.fields.TextField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'blog.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '250'})
        },
        u'blog.tag': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blog']