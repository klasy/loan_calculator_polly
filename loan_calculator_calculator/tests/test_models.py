from django.test import TestCase

from loan_calculator_calculator.calculator.models import Loan
from decimal import Decimal


class LoanModelsTestCase(TestCase):
    def test_model_save_positive(self):
        ll = Loan(purchase_price="100", interest_rate="5", down_payment_dollar="10", mortgage_term="5")

        # no errors are expected to be raised
        ll.save()

        # checking all the fields have been filled in
        self.assertIsNotNone(ll.monthly_payment)
        self.assertIsNotNone(ll.loan_amount)
        self.assertIsNotNone(ll.total_amount_paid)
        self.assertIsNotNone(ll.total_interest_paid)

        # we should also check the logic behind each calculation
        down_payment_percent = Decimal(ll.down_payment_dollar) * 100 / Decimal(ll.purchase_price)
        loan_amount = Decimal(ll.purchase_price) - Decimal(ll.down_payment_dollar)

        monthly_rate = Decimal(ll.interest_rate) / 12
        equity = (Decimal(ll.loan_amount) * monthly_rate) / (pow(monthly_rate + 1, ll.mortgage_term) - 1)

        monthly_payment = equity + ll.loan_amount * monthly_rate
        total_interest_paid = ll.loan_amount * Decimal(ll.interest_rate) / 100 * int(ll.mortgage_term)
        total_amount_paid = ll.monthly_payment * ll.mortgage_term

        self.assertEqual(ll.down_payment_percent, down_payment_percent)
        self.assertEqual(ll.loan_amount, loan_amount)
        self.assertEqual(ll.monthly_payment, monthly_payment)
        self.assertEqual(ll.total_interest_paid, total_interest_paid)
        self.assertEqual(ll.total_amount_paid, total_amount_paid)

    def test_cant_have_both_dollar_and_percent_together(self):
        ll = Loan(purchase_price="100", interest_rate="5", down_payment_dollar="10", down_payment_percent="10",
                  mortgage_term="5")
        with self.assertRaises(ValueError) as context:
            ll.save()

        self.assertEqual("Can't have both down payment in dollar value and percentage - please, choose one or the other",
                         str(context.exception))

    def test_no_down_payment_value(self):
        ll = Loan(purchase_price="100", interest_rate="5", mortgage_term="5")
        with self.assertRaises(ValueError) as context:
            ll.save()

        self.assertEqual(
            "Need to provide down payment value in either dollars or percentage",
            str(context.exception))
