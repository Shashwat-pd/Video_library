# Generated by Django 4.0.6 on 2022-07-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_video_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemproraryUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
