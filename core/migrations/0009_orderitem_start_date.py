# Generated by Django 2.1.5 on 2019-09-21 08:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_orderitem_ordered_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
