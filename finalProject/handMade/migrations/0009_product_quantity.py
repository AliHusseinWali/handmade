# Generated by Django 4.1.1 on 2022-10-28 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handMade', '0008_alter_product_title_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
