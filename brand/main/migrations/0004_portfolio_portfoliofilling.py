# Generated by Django 5.0.4 on 2024-04-24 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subheading', models.CharField(blank=True, max_length=255)),
                ('image_title', models.ImageField(blank=True, null=True, upload_to='portfolio/title/')),
                ('is_visible', models.BooleanField(default=True)),
                ('sort', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolio',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='PortfolioFilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subheading', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField()),
                ('image_full', models.ImageField(blank=True, null=True, upload_to='portfolio/full/')),
                ('date', models.CharField(blank=True, max_length=255)),
                ('client', models.CharField(blank=True, max_length=255)),
                ('category', models.CharField(blank=True, max_length=255)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to='main.portfolio')),
            ],
            options={
                'verbose_name': 'Info',
                'verbose_name_plural': 'Portfolio Filling',
                'ordering': ['title'],
            },
        ),
    ]
