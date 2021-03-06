# Generated by Django 3.1.3 on 2021-05-12 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EstateType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='estate name')),
                ('total_house', models.IntegerField(blank=True, null=True, verbose_name='total house')),
                ('street1', models.CharField(max_length=150, verbose_name='street 1')),
                ('city', models.CharField(max_length=20, verbose_name='city')),
                ('state_region', models.CharField(max_length=100, verbose_name='state or region')),
                ('country', models.CharField(max_length=100, verbose_name='country')),
                ('status', models.IntegerField(default=1, verbose_name='status')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='comment')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('estate_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.estatetype', verbose_name='')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='EstateAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perms', models.IntegerField(blank=True, null=True, verbose_name='permission')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admins', to='estate.estate', verbose_name='Estate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'unique_together': {('user', 'estate')},
            },
        ),
    ]
