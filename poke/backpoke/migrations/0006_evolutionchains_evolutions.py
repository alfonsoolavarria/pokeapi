# Generated by Django 3.1.5 on 2021-01-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backpoke', '0005_evolutionchains_evolves_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='evolutionchains',
            name='evolutions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
