# Generated by Django 5.0 on 2023-12-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0003_alter_cliente_updated_alter_producto_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
