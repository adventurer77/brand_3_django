# Generated by Django 5.0.4 on 2024-04-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='team/')),
                ('social_media_links', models.JSONField(blank=True, default=dict)),
                ('sort', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Team',
                'ordering': ['sort'],
            },
        ),
    ]