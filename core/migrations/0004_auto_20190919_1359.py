# Generated by Django 2.0 on 2019-09-19 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_orderitem_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='total',
            field=models.CharField(max_length=200),
        ),
    ]