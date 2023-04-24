# Generated by Django 4.1.7 on 2023-04-24 02:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workspace", "0001_initial"),
        ("board", "0002_remove_board_lists_board_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="workspace",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="workspace.workspace",
            ),
            preserve_default=False,
        ),
    ]
