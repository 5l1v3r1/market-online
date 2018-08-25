# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_usercheckout_braintree_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_total_currency',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_total_price_currency',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_total_price',
            field=models.DecimalField(default=5.99, max_digits=50, decimal_places=2),
        ),
    ]
