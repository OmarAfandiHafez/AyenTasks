from django.db import models


class MetaData(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    string = models.CharField(max_length=255, verbose_name='String')

    class Meta:
        verbose_name_plural = 'Meta Data'
        indexes = [models.Index(fields=('name',))]
        ordering = ('name', 'string')


class Document(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    file = models.FileField(upload_to='uploaded_files/')

    class Meta:
        indexes = [models.Index(fields=('name',))]
        ordering = ('name',)
