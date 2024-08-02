# Generated by Django 5.0.6 on 2024-07-27 11:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.CharField(choices=[('a', 'Accepted'), ('d', 'Declined'), ('u', 'Unprocessed')], default='u', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('base_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchange_offers', to='product.product')),
                ('exchange_for', models.ManyToManyField(to='product.product')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_owner', to=settings.AUTH_USER_MODEL)),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]