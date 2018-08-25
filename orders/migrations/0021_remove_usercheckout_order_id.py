# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20180714_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercheckout',
            name='order_id',
        ),
    ]
