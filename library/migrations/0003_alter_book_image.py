# Generated by Django 4.1.4 on 2022-12-29 18:38

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_url_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['top', 'left'], force_format=None, keep_meta=True, quality=-1, scale=None, size=[270, 400], upload_to='media/images'),
        ),
    ]
