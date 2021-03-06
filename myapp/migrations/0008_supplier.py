# Generated by Django 2.0.13 on 2019-03-02 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_order_order_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_id', models.CharField(max_length=10)),
                ('supplier_name', models.CharField(max_length=200)),
                ('supplier_email', models.EmailField(max_length=254)),
                ('supplier_time', models.IntegerField(default=10)),
            ],
        ),
    ]
