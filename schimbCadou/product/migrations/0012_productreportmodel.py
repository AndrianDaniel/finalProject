# Generated by Django 5.0.6 on 2024-08-03 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_walletmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(max_length=450)),
                ('resolution', models.CharField(choices=[('r', 'Resolved'), ('d', 'Declined'), ('u', 'Unprocessed')], default='u', max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
