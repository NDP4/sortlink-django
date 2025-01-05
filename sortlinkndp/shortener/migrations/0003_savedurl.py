# Generated by Django 5.1.4 on 2024-12-31 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_urlvisit'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener.shortenedurl')),
            ],
            options={
                'ordering': ['-saved_at'],
            },
        ),
    ]
