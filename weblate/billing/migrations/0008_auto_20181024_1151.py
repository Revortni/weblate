# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 09:51
from __future__ import unicode_literals

from django.db import migrations

import weblate.utils.fields


class Migration(migrations.Migration):

    dependencies = [("billing", "0007_plan_public")]

    operations = [
        migrations.AlterField(
            model_name="billing",
            name="payment",
            field=weblate.utils.fields.JSONField(default={}, editable=False),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="payment",
            field=weblate.utils.fields.JSONField(default={}, editable=False),
        ),
    ]
