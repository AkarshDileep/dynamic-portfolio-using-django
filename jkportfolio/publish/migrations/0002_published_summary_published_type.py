# Generated by Django 5.0.6 on 2024-06-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='published',
            name='summary',
            field=models.TextField(default='default summary text'),
        ),
        migrations.AddField(
            model_name='published',
            name='type',
            field=models.CharField(default='project', max_length=100),
        ),
    ]
