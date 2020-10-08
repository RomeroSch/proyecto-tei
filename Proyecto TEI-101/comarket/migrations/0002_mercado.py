# Generated by Django 2.2.4 on 2020-07-05 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comarket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mercado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.PositiveIntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('lugar', models.CharField(max_length=100)),
                ('precio', models.PositiveIntegerField()),
                ('descripcion', models.TextField(max_length=250)),
            ],
        ),
    ]