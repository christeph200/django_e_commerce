# Generated by Django 2.2.13 on 2020-11-20 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discountprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test description'),
            preserve_default=False,
        ),
    ]