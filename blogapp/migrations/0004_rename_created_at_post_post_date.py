# Generated by Django 4.1.5 on 2024-07-16 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0003_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="created_at",
            new_name="post_date",
        ),
    ]
