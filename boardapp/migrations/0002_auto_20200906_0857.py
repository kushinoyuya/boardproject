# Generated by Django 3.0.3 on 2020-09-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='good',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='read',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='readtext',
            field=models.IntegerField(blank=True, default='a', max_length=200, null=True),
        ),
    ]
