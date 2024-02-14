# Generated by Django 4.2.9 on 2024-02-14 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfume_review', '0007_alter_perfume_concentration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfume',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='perfume',
            name='image_alt',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='concentration',
            field=models.CharField(choices=[('eau fraiche', 'Eau Fraiche'), ('eau de cologne', 'Eau de Cologne'), ('eau de toilette', 'Eau de Toilette'), ('eau de parfum', 'Eau de Parfum'), ('parfum', 'Parfum'), ('extrait de parfum', 'Extrait de Parfum')], default='eau de parfum', max_length=50),
        ),
    ]
