# Generated by Django 4.2.11 on 2024-05-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newspaper", "0005_newspaper_image_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="redactor",
            name="years_of_experience",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
