# Generated by Django 5.0.6 on 2024-05-31 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='website_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
