# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table(u'blog_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
        ))
        db.send_create_signal(u'blog', ['Link'])

        # Adding model 'Tag'
        db.create_table(u'blog_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
        ))
        db.send_create_signal(u'blog', ['Tag'])

        # Adding model 'Entry'
        db.create_table(u'blog_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('markdown', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'blog', ['Entry'])

        # Adding M2M table for field tags on 'Entry'
        db.create_table(u'blog_entry_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entry', models.ForeignKey(orm[u'blog.entry'], null=False)),
            ('tag', models.ForeignKey(orm[u'blog.tag'], null=False))
        ))
        db.create_unique(u'blog_entry_tags', ['entry_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table(u'blog_link')

        # Deleting model 'Tag'
        db.delete_table(u'blog_tag')

        # Deleting model 'Entry'
        db.delete_table(u'blog_entry')

        # Removing M2M table for field tags on 'Entry'
        db.delete_table('blog_entry_tags')


    models = {
        u'blog.entry': {
            'Meta': {'ordering': "['-date', 'title']", 'object_name': 'Entry'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'markdown': ('django.db.models.fields.TextField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        },
        u'blog.tag': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']