# Generated by Django 4.2.7 on 2023-11-11 03:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "categories"},
        ),
        migrations.RemoveField(
            model_name="page",
            name="slug",
        ),
    ]