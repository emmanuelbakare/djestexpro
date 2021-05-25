# Generated by Django 3.1.3 on 2021-05-18 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estate', '0003_auto_20210512_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='admin',
            field=models.ManyToManyField(through='estate.EstateAdmin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='estateadmin',
            name='estate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.estate', verbose_name='Estate'),
        ),
        migrations.AlterField(
            model_name='estateadmin',
            name='perms',
            field=models.IntegerField(default=1, verbose_name='permission'),
        ),
    ]
