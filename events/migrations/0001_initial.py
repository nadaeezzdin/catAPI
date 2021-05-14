# Generated by Django 3.2 on 2021-05-13 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ar', models.CharField(max_length=255, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ar', models.TextField(null=True)),
                ('sessionlink', models.URLField(blank=True)),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='events.event')),
                ('event_name_ar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='events.event')),
                ('event_name_en', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='EventPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('session_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventsession', to='events.eventsession')),
            ],
        ),
    ]
