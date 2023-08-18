# Generated by Django 4.2.4 on 2023-08-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_image_alter_category_category_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'Subcategories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='images/'),
        ),
    ]