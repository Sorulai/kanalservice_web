# Generated by Django 4.0.6 on 2022-07-30 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_cost_rub',
            field=models.FloatField(verbose_name='Стоимость заказа, RUB'),
        ),
    ]
