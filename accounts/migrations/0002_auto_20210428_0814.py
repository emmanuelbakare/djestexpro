# Generated by Django 3.1.3 on 2021-04-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='defaultUser.png', upload_to='profile_pix', verbose_name='profile picture'),
        ),
    ]
