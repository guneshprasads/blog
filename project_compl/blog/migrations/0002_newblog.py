# Generated by Django 3.1 on 2020-08-31 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogname', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]