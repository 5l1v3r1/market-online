# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_order_braintree_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercheckout',
            name='braintree_id',
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=120, null=True, verbose_name=orders.models.UserCheckout),
        ),
        migrations.AlterField(
            model_name='order',
            name='braintree_id',
            field=models.CharField(max_length=120, null=True, verbose_name=orders.models.UserCheckout, blank=True),
        ),
    ]
