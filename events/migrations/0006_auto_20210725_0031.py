# Generated by Django 3.2 on 2021-07-24 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_eventsession_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventsession',
            name='event_ar',
        ),
        migrations.RemoveField(
            model_name='eventsession',
            name='event_en',
        ),
    ]