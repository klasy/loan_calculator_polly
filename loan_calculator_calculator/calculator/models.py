from django.db import models
from decimal import Decimal


# Create your models here.
class Loan(models.Model):
    # input fields
    purchase_price = models.DecimalField(max_digits=15, decimal_places=3)
    interest_rate = models.DecimalField(max_digits=6, decimal_places=2)
    down_payment_dollar = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True)
    down_payment_percent = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True)
    mortgage_term = models.IntegerField()

    # additional fields needed for the output/logic
    monthly_payment = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True)
    loan_amount = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    total_amount_paid = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True)
    total_interest_paid = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.down_payment_dollar and self.down_payment_percent:
            raise ValueError("Can't have both down payment in dollar value and percentage - please, choose one or the other")

        if not self.down_payment_percent and not self.down_payment_dollar:
            raise ValueError("Need to provide down payment value in either dollars or percentage")

        if self.down_payment_dollar:
            self.down_payment_percent = Decimal(self.down_payment_dollar) * 100 / Decimal(self.purchase_price)
        elif self.down_payment_percent:
            self.down_payment_dollar = Decimal(self.purchase_price) * Decimal(self.down_payment_percent) / 100

        self.loan_amount = Decimal(self.purchase_price) - Decimal(self.down_payment_dollar)

        monthly_rate = Decimal(self.interest_rate) / 12
        equity = (Decimal(self.loan_amount) * monthly_rate) / (pow(monthly_rate + 1, self.mortgage_term) - 1)

        self.monthly_payment = equity + self.loan_amount * monthly_rate
        self.total_interest_paid = self.loan_amount * Decimal(self.interest_rate) / 100 * int(self.mortgage_term)
        self.total_amount_paid = self.monthly_payment * self.mortgage_term

        super(Loan, self).save(force_insert, force_update, using, update_fields)
