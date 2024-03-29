# Generated by Django 4.2.9 on 2024-02-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("perfume_review", "0005_alter_perfume_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="perfume",
            name="concentration",
            field=models.CharField(
                choices=[
                    ("eau_fraiche", "Eau Fraiche"),
                    ("eau_de_cologne", "Eau de Cologne"),
                    ("eau_de_toilette", "Eau de Toilette"),
                    ("eau de parfum", "Eau de Parfum"),
                    ("parfum", "Parfum"),
                    ("extrait_de_parfum", "Extrait de Parfum"),
                ],
                default="eau_de_toilette",
                max_length=50,
            ),
        ),
    ]
