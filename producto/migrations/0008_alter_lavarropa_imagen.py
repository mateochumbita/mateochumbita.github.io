# Generated by Django 4.1.5 on 2023-01-24 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0007_alter_lavarropa_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lavarropa',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
