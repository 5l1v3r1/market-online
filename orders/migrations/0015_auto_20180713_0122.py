# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20180712_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(null=True, max_digits=50, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_total_price',
            field=models.DecimalField(default=5.99, null=True, max_digits=50, decimal_places=2, blank=True),
        ),
    ]
