# Generated by Django 3.0.3 on 2020-09-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0002_auto_20200906_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='readtext',
            field=models.CharField(blank=True, default='a', max_length=200, null=True),
        ),
    ]
