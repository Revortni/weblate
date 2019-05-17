# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 12:46
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import weblate.trans.fields
import weblate.utils.validators


class Migration(migrations.Migration):

    replaces = [
        ("weblate_auth", "0002_auto_20180507_1540"),
        ("weblate_auth", "0003_permissions"),
        ("weblate_auth", "0004_auto_20180508_1032"),
        ("weblate_auth", "0005_groups"),
        ("weblate_auth", "0006_autogroup"),
        ("weblate_auth", "0007_auto_20180509_0739"),
        ("weblate_auth", "0008_email_fixup"),
        ("weblate_auth", "0009_auto_20180509_1552"),
        ("weblate_auth", "0010_auto_20180509_1630"),
        ("weblate_auth", "0011_auto_20180509_0739"),
    ]

    dependencies = [
        ("weblate_auth", "0001_initial"),
        ("trans", "0131_auto_20180416_1610"),
        ("lang", "0011_auto_20180215_1158"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=150, unique=True, verbose_name="Name"),
                ),
                (
                    "project_selection",
                    models.IntegerField(
                        choices=[
                            (0, "As defined"),
                            (1, "All projects"),
                            (3, "All public projects"),
                            (4, "All protected projects"),
                            (2, "From component list"),
                        ],
                        default=0,
                        verbose_name="Project selection",
                    ),
                ),
                (
                    "language_selection",
                    models.IntegerField(
                        choices=[(0, "As defined"), (1, "All languages")],
                        default=0,
                        verbose_name="Language selection",
                    ),
                ),
                (
                    "internal",
                    models.BooleanField(
                        default=False, verbose_name="Weblate internal group"
                    ),
                ),
                (
                    "componentlist",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.ComponentList",
                        verbose_name="Component list",
                    ),
                ),
                (
                    "languages",
                    models.ManyToManyField(
                        blank=True, to="lang.Language", verbose_name="Languages"
                    ),
                ),
                (
                    "projects",
                    models.ManyToManyField(
                        blank=True, to="trans.Project", verbose_name="Projects"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Permission",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codename", models.CharField(max_length=100, unique=True)),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "ordering": ["codename"],
                "verbose_name": "Permission",
                "verbose_name_plural": "Permissions",
            },
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Name")),
                (
                    "permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Choose permissions granted to this role.",
                        to="weblate_auth.Permission",
                        verbose_name="Permissions",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="group",
            name="roles",
            field=models.ManyToManyField(
                blank=True,
                help_text="Choose roles granted to this group.",
                to="weblate_auth.Role",
                verbose_name="Roles",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The user is granted all permissions included in membership of these groups.",
                to="weblate_auth.Group",
                verbose_name="Groups",
            ),
        ),
        migrations.CreateModel(
            name="AutoGroup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "match",
                    weblate.trans.fields.RegexField(
                        default="^.*$",
                        help_text="Regular expression used to match user email.",
                        max_length=200,
                        verbose_name="Email regular expression",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="weblate_auth.Group",
                        verbose_name="Group to assign",
                    ),
                ),
            ],
            options={
                "ordering": ("group__name",),
                "verbose_name": "Automatic group assignment",
                "verbose_name_plural": "Automatic group assignments",
            },
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=190,
                unique=True,
                validators=[weblate.utils.validators.validate_email],
                verbose_name="Email",
            ),
        ),
    ]
