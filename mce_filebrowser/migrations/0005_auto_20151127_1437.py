# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mce_filebrowser.models


class Migration(migrations.Migration):

    dependencies = [
        ('mce_filebrowser', '0004_add_tags_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filebrowserfile',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create date'),
        ),
        migrations.AlterField(
            model_name='filebrowserfile',
            name='file_type',
            field=models.CharField(max_length=3, choices=[('img', 'Image'), ('doc', 'Document')]),
        ),
        migrations.AlterField(
            model_name='filebrowserfile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='filebrowserfile',
            name='uploaded_file',
            field=models.FileField(max_length=300, upload_to=mce_filebrowser.models.content_file_name, verbose_name='File / Image'),
        ),
        migrations.AlterField(
            model_name='filebrowserfile',
            name='user_id',
            field=models.IntegerField(null=True, verbose_name='Who does this file belong to?', blank=True),
        ),
    ]