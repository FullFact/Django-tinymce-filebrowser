# -*- coding: utf-8 -*-
import datetime
# from south.db import db
# from south.v2 import SchemaMigration
from django.db import models, migrations
from taggit.managers import TaggableManager
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mce_filebrowser', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='FileBrowserFile',
            name='user_id',
            field=models.ForeignKey(on_delete=models.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
#     def forwards(self, orm):
#         # Adding field 'FileBrowserFile.user_id'
#         db.add_column(u'mce_filebrowser_filebrowserfile', 'user_id',
#                       self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
#                       keep_default=False)


#     def backwards(self, orm):
#         # Deleting field 'FileBrowserFile.user_id'
#         db.delete_column(u'mce_filebrowser_filebrowserfile', 'user_id')


#     models = {
#         u'mce_filebrowser.filebrowserfile': {
#             'Meta': {'object_name': 'FileBrowserFile'},
#             'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
#             'file_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
#             u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
#             'uploaded_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
#             'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
#         }
#     }

#     complete_apps = ['mce_filebrowser']