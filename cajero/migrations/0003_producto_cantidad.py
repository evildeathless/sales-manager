# Generated by Django 3.1.6 on 2021-03-02 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cajero', '0002_arqueo_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.PositiveIntegerField(default=20),
        ),
    ]