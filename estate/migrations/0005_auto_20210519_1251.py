# Generated by Django 3.1.3 on 2021-05-19 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0004_auto_20210518_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estate',
            old_name='admin',
            new_name='admins',
        ),
    ]
