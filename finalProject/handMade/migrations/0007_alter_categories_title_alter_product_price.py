# Generated by Django 4.1.1 on 2022-10-22 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handMade', '0006_remove_categories_name_categories_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.ForeignKey(blank=True, db_column='Main category', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='handMade.categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
