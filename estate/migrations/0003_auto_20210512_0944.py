# Generated by Django 3.1.3 on 2021-05-12 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_auto_20210512_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='estate_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.estatetype'),
        ),
    ]