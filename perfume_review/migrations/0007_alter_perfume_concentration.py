# Generated by Django 4.2.9 on 2024-02-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("perfume_review", "0006_alter_perfume_concentration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="perfume",
            name="concentration",
            field=models.CharField(
                choices=[
                    ("eau fraiche", "Eau Fraiche"),
                    ("eau de cologne", "Eau de Cologne"),
                    ("eau de toilette", "Eau de Toilette"),
                    ("eau de parfum", "Eau de Parfum"),
                    ("parfum", "Parfum"),
                    ("extrait de parfum", "Extrait de Parfum"),
                ],
                default="eau_de_toilette",
                max_length=50,
            ),
        ),
    ]
