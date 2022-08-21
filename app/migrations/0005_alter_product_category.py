# Generated by Django 4.0.1 on 2022-03-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_product_category_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('MN', 'Men'), ('WM', 'Women'), ('KD', 'Kids')], max_length=2, null=True),
        ),
    ]
