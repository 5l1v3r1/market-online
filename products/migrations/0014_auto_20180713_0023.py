# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20180712_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='price',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
    ]
