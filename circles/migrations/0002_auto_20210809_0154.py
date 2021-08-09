# Generated by Django 3.2.6 on 2021-08-08 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nontechcircle',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='nontechcircle',
            name='title_ar',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='nontechcircle',
            name='title_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='techcircle',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='techcircle',
            name='title_ar',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='techcircle',
            name='title_en',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
