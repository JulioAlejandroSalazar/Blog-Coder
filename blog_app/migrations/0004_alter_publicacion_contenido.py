# Generated by Django 4.0.6 on 2022-10-01 01:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_rename_username_publicacion_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='contenido',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
