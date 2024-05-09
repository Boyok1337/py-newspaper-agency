# Generated by Django 4.2.11 on 2024-05-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_newspaper_image_url_alter_newspaper_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]