# Generated by Django 4.2.9 on 2024-02-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfume_review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfume',
            name='concentration',
            field=models.CharField(choices=[('eau_fraiche', 'Eau Fraiche'), ('eau_de_cologne', 'Eau de Cologne'), ('eau_de_toilette', 'Eau de Toilette'), ('eau_de_parfum', 'Eau de Parfum'), ('parfum', 'Parfum'), ('extrait_de_parfum', 'Extrait de Parfum')], default='eau_de_toilette', max_length=50),
        ),
    ]