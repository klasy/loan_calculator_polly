# Generated by Django 5.0.6 on 2024-06-21 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='down_payment_dollar',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='down_payment_percent',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='interest_rate',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_amount',
            field=models.DecimalField(decimal_places=3, max_digits=15),
        ),
        migrations.AlterField(
            model_name='loan',
            name='monthly_payment',
            field=models.DecimalField(decimal_places=3, max_digits=12),
        ),
        migrations.AlterField(
            model_name='loan',
            name='purchase_price',
            field=models.DecimalField(decimal_places=3, max_digits=15),
        ),
        migrations.AlterField(
            model_name='loan',
            name='total_amount_paid',
            field=models.DecimalField(decimal_places=3, max_digits=12),
        ),
        migrations.AlterField(
            model_name='loan',
            name='total_interest_paid',
            field=models.DecimalField(decimal_places=3, max_digits=12),
        ),
    ]
