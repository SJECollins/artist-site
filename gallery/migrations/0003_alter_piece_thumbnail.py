# Generated by Django 3.2.16 on 2023-01-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20230109_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/thumbs/'),
        ),
    ]
