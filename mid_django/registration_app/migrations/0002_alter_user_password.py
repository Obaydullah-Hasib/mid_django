# Generated by Django 4.2.3 on 2023-08-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=64),
        ),
    ]
