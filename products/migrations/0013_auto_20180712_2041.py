# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20180612_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_currency',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='price_currency',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='sale_price_currency',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='variation',
            name='price',
            field=models.DecimalField(max_digits=20, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='variation',
            name='sale_price',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
    ]
