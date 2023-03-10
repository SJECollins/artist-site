# Generated by Django 3.2.16 on 2023-01-09 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=280)),
                ('slug', models.CharField(max_length=140)),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('date_start', models.DateField(blank=True, null=True)),
                ('date_end', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('collection_name',),
            },
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece_name', models.CharField(max_length=280)),
                ('slug', models.CharField(max_length=140)),
                ('size', models.CharField(blank=True, max_length=140, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.collection')),
            ],
            options={
                'ordering': ('collection',),
            },
        ),
    ]
