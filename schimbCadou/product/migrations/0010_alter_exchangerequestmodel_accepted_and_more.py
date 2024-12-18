# Generated by Django 5.0.6 on 2024-07-28 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_exchangerequestmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerequestmodel',
            name='accepted',
            field=models.CharField(choices=[('a', 'Accepted'), ('d', 'Declined'), ('u', 'Unprocessed')], default='u', max_length=1),
        ),
        migrations.AlterField(
            model_name='exchangerequestmodel',
            name='exchange_for',
            field=models.ManyToManyField(related_name='exchange_offers_for', to='product.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]
