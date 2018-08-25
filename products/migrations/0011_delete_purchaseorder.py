# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_purchaseorder'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PurchaseOrder',
        ),
    ]
