# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-21 09:03
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("trans", "0018_remove_unusednewbase_alert")]

    operations = [
        migrations.AddField(
            model_name="change",
            name="comment",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="trans.Comment",
            ),
        ),
        migrations.AddField(
            model_name="change",
            name="suggestion",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="trans.Suggestion",
            ),
        ),
    ]
