# Generated by Django 3.2 on 2021-05-21 02:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mpsapps', '0010_sgpstaff_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CafiMembro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naran', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='membro_cafi')),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='fundomodel',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
