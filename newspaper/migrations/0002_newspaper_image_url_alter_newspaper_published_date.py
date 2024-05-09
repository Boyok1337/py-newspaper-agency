# Generated by Django 4.2.11 on 2024-05-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspaper',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newspaper',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
