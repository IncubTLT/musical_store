# Generated by Django 4.1.7 on 2023-04-20 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_group_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='groups', to='products.group'),
            preserve_default=False,
        ),
    ]
