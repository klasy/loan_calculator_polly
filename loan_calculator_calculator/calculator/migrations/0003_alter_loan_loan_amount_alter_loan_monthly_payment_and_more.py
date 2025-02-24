# Generated by Django 5.0.6 on 2024-06-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_alter_loan_down_payment_dollar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_amount',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='monthly_payment',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='total_amount_paid',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='total_interest_paid',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True),
        ),
    ]
