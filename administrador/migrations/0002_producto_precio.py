# Generated by Django 4.2.2 on 2023-07-05 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]
