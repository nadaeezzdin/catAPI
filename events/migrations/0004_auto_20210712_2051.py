# Generated by Django 3.2 on 2021-07-12 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210513_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventsession',
            old_name='event_name',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='eventsession',
            old_name='event_name_ar',
            new_name='event_ar',
        ),
        migrations.RenameField(
            model_name='eventsession',
            old_name='event_name_en',
            new_name='event_en',
        ),
        migrations.AlterField(
            model_name='eventphoto',
            name='session_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventsessionphotos', to='events.eventsession'),
        ),
    ]
