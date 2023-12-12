# Generated by Django 4.1.13 on 2023-12-11 19:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_profile_phone_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="photo",
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(blank=True, max_length=11),
        ),
    ]