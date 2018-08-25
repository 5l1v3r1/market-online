# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_usercheckout_braintree_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='braintree_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.AddField(
            model_name='usercheckout',
            name='order_id',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
