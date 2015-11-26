# -*- coding: utf-8 -*-
import datetime
# from south.db import db
# from south.v2 import SchemaMigration
from django.db import models, migrations
from taggit.managers import TaggableManager


class Migration(migrations.Migration):

    # def forwards(self, orm):
    #     # Adding model 'FileBrowserFile'
    #     db.create_table(u'mce_filebrowser_filebrowserfile', (
    #         (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
    #         ('file_type', self.gf('django.db.models.fields.CharField')(max_length=3)),
    #         ('uploaded_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
    #         ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
    #     ))
    #     db.send_create_signal(u'mce_filebrowser', ['FileBrowserFile'])


    # def backwards(self, orm):
    #     # Deleting model 'FileBrowserFile'
    #     db.delete_table(u'mce_filebrowser_filebrowserfile')


    # models = {
    #     u'mce_filebrowser.filebrowserfile': {
    #         'Meta': {'object_name': 'FileBrowserFile'},
    #         'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
    #         'file_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
    #         u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
    #         'uploaded_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
    #     }
    # }

    # complete_apps = ['mce_filebrowser']

    operations = [
        migrations.CreateModel(
            name='FileBrowserFile',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('file_type', models.CharField(max_length=3)),
                ('uploaded_file', models.FileField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True, blank=True)),
                ('tags', TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag')),
            ]
                
        )
    ]
