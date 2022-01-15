# Generated by Django 4.0.1 on 2022-01-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='Group', max_length=30),
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(to='api.Profile'),
        ),
        migrations.AddField(
            model_name='movement',
            name='description',
            field=models.CharField(default='Movement', max_length=100),
        ),
    ]
