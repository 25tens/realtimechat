from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
#from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=200,default='',blank=True)
#    description = models.TextField(default='',blank=True)
#    photo = models.ImageField(blank=True, null=True)
#    description = RichTextField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
#    description2 = RichTextUploadingField(blank=True, null=True,config_name='special')
    description2 = RichTextUploadingField(blank=True,
                                          null=True, 
                                          config_name='special',
                                          external_plugin_resources=[(  
                                              'youtube',
                                              '/static/vendor/ckeditor_plugins/youtube/youtube/',
                                              'plugin.js',
                                          )],
                                         )
#   text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return '%s'% self.title;