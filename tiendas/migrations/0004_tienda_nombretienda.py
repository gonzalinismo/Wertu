# Generated by Django 2.1.7 on 2019-06-04 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendas', '0003_auto_20190531_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='nombreTienda',
            field=models.CharField(default='test', max_length=100),
        ),
    ]
