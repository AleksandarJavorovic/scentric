# Generated by Django 4.2.9 on 2024-02-06 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("perfume_review", "0002_perfume_concentration"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="perfume",
            name="rating",
        ),
        migrations.AlterField(
            model_name="perfume",
            name="slug",
            field=models.SlugField(default="", max_length=200),
        ),
    ]
