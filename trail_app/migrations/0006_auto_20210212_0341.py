# Generated by Django 3.0.6 on 2021-02-12 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trail_app', '0005_auto_20210211_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='spot_on_trail',
        ),
        migrations.AddField(
            model_name='trail',
            name='trail_spots',
            field=models.ManyToManyField(blank=True, null=True, to='trail_app.Spot'),
        ),
        migrations.AddField(
            model_name='trail_group',
            name='tg_trail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trail_app.Trail'),
        ),
    ]