# Generated by Django 2.1.5 on 2019-03-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='start_x',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='start_y',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
