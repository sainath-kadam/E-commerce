# Generated by Django 4.0.1 on 2022-03-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_product_brand_remove_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('MN', 'Men'), ('WM', 'Women'), ('KD', 'Kids')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='app/images'),
        ),
    ]
