# Generated by Django 3.2.25 on 2025-06-10 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_publicacion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
    ]
