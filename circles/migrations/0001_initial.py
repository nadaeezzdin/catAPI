# Generated by Django 3.2 on 2021-05-14 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NonTechCircle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('title_ar', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ar', models.TextField(null=True)),
                ('skills', models.TextField()),
                ('skills_en', models.TextField(null=True)),
                ('skills_ar', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechCircle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('title_ar', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ar', models.TextField(null=True)),
                ('RMlink', models.URLField()),
                ('designtools', models.TextField()),
                ('designtools_en', models.TextField(null=True)),
                ('designtools_ar', models.TextField(null=True)),
            ],
        ),
    ]
