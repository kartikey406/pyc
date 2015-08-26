# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
        migrations.DeleteModel(
            name='Details',
        ),
    ]
