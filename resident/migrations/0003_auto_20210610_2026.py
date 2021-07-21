# Generated by Django 3.1.3 on 2021-06-10 19:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0005_auto_20210519_1251'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resident', '0002_auto_20210603_2012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resident',
            options={'ordering': ['estate']},
        ),
        migrations.AlterUniqueTogether(
            name='resident',
            unique_together={('estate', 'user')},
        ),
    ]
