# Generated by Django 4.2.4 on 2023-08-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_user_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_super",
            field=models.BooleanField(default=False),
        ),
    ]
