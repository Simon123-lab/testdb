# Generated by Django 3.2.2 on 2021-12-15 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image_data',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]