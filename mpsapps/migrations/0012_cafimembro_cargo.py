# Generated by Django 3.2 on 2021-05-21 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpsapps', '0011_auto_20210521_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafimembro',
            name='cargo',
            field=models.CharField(blank=True, choices=[('presidente', 'presidente'), ('membro', 'presidente')], max_length=50),
        ),
    ]
