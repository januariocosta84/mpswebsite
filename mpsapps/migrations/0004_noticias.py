# Generated by Django 3.2 on 2021-05-19 01:58

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpsapps', '0003_sgpmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='noticias')),
                ('konteudu', ckeditor_uploader.fields.RichTextUploadingField()),
                ('data', models.DateField(auto_now=True)),
            ],
        ),
    ]
