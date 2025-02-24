# Generated by Django 3.0.3 on 2020-04-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('file', models.FileField(upload_to='uploaded_files/')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('string', models.CharField(max_length=255, verbose_name='String')),
            ],
            options={
                'verbose_name_plural': 'Meta Data',
                'ordering': ('name', 'string'),
            },
        ),
        migrations.AddIndex(
            model_name='metadata',
            index=models.Index(fields=['name'], name='api_metadat_name_17aedd_idx'),
        ),
        migrations.AddIndex(
            model_name='document',
            index=models.Index(fields=['name'], name='api_documen_name_61fbf9_idx'),
        ),
    ]
