# Generated by Django 4.1.7 on 2023-02-28 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almendra_app', '0027_cafes_model_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cafes_model',
            old_name='info',
            new_name='informacion',
        ),
        migrations.RenameField(
            model_name='populares_model',
            old_name='info',
            new_name='informacion',
        ),
    ]
