# Generated by Django 3.2 on 2021-05-21 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpsapps', '0008_sgpstaff_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sgpstaff',
            old_name='staff',
            new_name='image',
        ),
    ]
