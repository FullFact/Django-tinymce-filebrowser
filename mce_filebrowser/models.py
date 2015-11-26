import datetime

from django.db import models
from django.utils.translation import ugettext as _
from taggit.managers import TaggableManager

from mce_filebrowser.conf import LOCAL_MCE_FILEBROWSER_UPLOADDIR,LOCAL_MCE_FILEBROWSER_PERUSER


def content_file_name(instance, filename):
    return "%s/%s" %(LOCAL_MCE_FILEBROWSER_UPLOADDIR, filename)


class FileBrowserFile(models.Model):
    """ Uploaded file model """
    FILE_TYPES = (
        ('img', _('Image')),
        ('doc', _('Document')),
    )

    file_type = models.CharField(max_length=3, choices=FILE_TYPES)
    uploaded_file = models.FileField(
        upload_to=content_file_name,
        verbose_name = _('File / Image'),
        max_length=300,
    )
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Create date')
    )

    user_id = models.IntegerField(null=True, blank=True, verbose_name=_('Who does this file belong to?'))
    tags = TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag')

    def __unicode__(self):
        return u'%s' % self.uploaded_file.name
