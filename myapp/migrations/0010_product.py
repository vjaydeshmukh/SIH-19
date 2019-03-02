# Generated by Django 2.0.13 on 2019-03-02 10:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_supplier_supplier_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=10)),
                ('product_type', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', max_length=1)),
                ('main_order_date', models.DateField(default=datetime.datetime(2019, 3, 2, 10, 6, 21, 917013, tzinfo=utc))),
                ('completion_date', models.DateField()),
                ('recieved_date', models.DateField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='myapp.Supplier')),
            ],
        ),
    ]