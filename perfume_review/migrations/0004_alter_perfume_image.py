# Generated by Django 4.2.9 on 2024-02-11 11:02

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('perfume_review', '0003_remove_perfume_rating_alter_perfume_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[300, None], upload_to='perfume_reviwes/'),
        ),
    ]