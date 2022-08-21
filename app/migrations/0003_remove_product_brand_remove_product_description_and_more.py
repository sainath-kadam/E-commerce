# Generated by Django 4.0.1 on 2022-03-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cart_product_orderplaced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discounted_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='selling_pricerice',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
