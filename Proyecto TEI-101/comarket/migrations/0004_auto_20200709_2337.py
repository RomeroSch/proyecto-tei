# Generated by Django 2.2.4 on 2020-07-10 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comarket', '0003_mercado_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercado',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]