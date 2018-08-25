# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20180628_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='Phone',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
