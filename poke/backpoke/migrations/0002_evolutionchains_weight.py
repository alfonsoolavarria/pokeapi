# Generated by Django 3.1.5 on 2021-01-19 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backpoke', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evolutionchains',
            name='weight',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
