# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20180623_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='tax_percentage_currency',
        ),
        migrations.AlterField(
            model_name='cart',
            name='tax_percentage',
            field=models.DecimalField(default=0.085, max_digits=10, decimal_places=5),
        ),
    ]
