# -*- coding: utf-8 -*-
import datetime
# from south.db import db
# from south.v2 import SchemaMigration
from django.db import models, migrations
from taggit.managers import TaggableManager


class Migration(migrations.Migration):
    dependencies = [
        ('taggit', '0003_auto__chg_field_filebrowserfile_uploaded_file'),
    ]
    
    operations = [
        migrations.AddField(
            model_name='file_browser_file',
            name='tags',
            field=TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag'),
        ),
    ]