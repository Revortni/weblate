# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-07 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("billing", "0011_billing_grace_period")]

    operations = [
        migrations.AlterField(
            model_name="billing",
            name="state",
            field=models.IntegerField(
                choices=[
                    (0, "Active"),
                    (1, "Trial"),
                    (2, "Expired"),
                    (3, "Terminated"),
                ],
                default=0,
                verbose_name="Billing state",
            ),
        )
    ]
