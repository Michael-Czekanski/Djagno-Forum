# Generated by Django 3.1.7 on 2021-03-06 11:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_post_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
