# Generated by Django 5.1.7 on 2025-03-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='name',
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(default='No Subject', max_length=255),
        ),
    ]
