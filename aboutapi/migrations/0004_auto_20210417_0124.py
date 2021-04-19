# Generated by Django 3.2 on 2021-04-16 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutapi', '0003_auto_20210416_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutteam',
            options={'verbose_name': 'aboutTeam'},
        ),
        migrations.AlterModelOptions(
            name='aboutteamtranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'aboutTeam Translation'},
        ),
        migrations.AlterModelOptions(
            name='circles',
            options={'verbose_name': 'circles'},
        ),
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name': 'events'},
        ),
        migrations.AlterModelOptions(
            name='headsinfo',
            options={'verbose_name': 'headsInfo'},
        ),
        migrations.AlterModelOptions(
            name='headsinfotranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'headsInfo Translation'},
        ),
        migrations.AlterModelOptions(
            name='topmembers',
            options={'verbose_name': 'topMembers'},
        ),
        migrations.AlterModelOptions(
            name='topmemberstranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'topMembers Translation'},
        ),
    ]
