# Generated by Django 3.1.4 on 2021-06-02 08:17

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpsapps', '0029_programas'),
    ]

    operations = [
        migrations.AddField(
            model_name='programas',
            name='konteudu_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='programas',
            name='konteudu_pt',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='programas',
            name='konteudu_tt',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='programas',
            name='slug_en',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='programas',
            name='slug_pt',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='programas',
            name='slug_tt',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='programas',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='programas',
            name='title_pt',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='programas',
            name='title_tt',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
