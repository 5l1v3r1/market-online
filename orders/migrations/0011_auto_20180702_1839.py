# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_useraddress_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='Phone',
            new_name='phone',
        ),
    ]
