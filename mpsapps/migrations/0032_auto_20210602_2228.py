# Generated by Django 3.2 on 2021-06-02 13:28

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpsapps', '0031_infoprogramas'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoprogramas',
            name='konteudu_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='infoprogramas',
            name='konteudu_pt',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='infoprogramas',
            name='konteudu_tt',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='infoprogramas',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='infoprogramas',
            name='title_pt',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='infoprogramas',
            name='title_tt',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
