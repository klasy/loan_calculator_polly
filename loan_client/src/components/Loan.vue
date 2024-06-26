<template>

<h1>Loan Payment Calculator</h1>

<div class="container">

<div class="flex-item">
<form ref="loanForm" @submit.prevent="createLoan" class="loanForm">
   <p>
      <label>Purchase Price *</label>
   </p>
   <p>
      <input type="number" placeholder="E.g. $ 100,000.000" v-model.number="purchasePrice" required />
   </p>
   <p>
      <label>Interest Rate *</label>
   </p>
   <p>
      <input type="number" placeholder="E.g. 20 %" v-model.number="interestRate" required />
   </p>
   <p>
      <label>Down Payment in $</label>
   </p>
   <p>
      <input type="number" placeholder="E.g. $ 15,000.000" v-model.number="downPaymentDollar" />
   </p>
   <p>
      <label>Down Payment in %</label>
   </p>
   <p>
      <input type="number" placeholder="E.g. 20 %" v-model.number="downPaymentPercent" />
   </p>
   <p>
      <label>Mortgage Term *</label>
   </p>
   <p>
      <input type="number" placeholder="E.g. 90 months" v-model.number="mortgageTerm" required />
   </p>
   <p>
      <button type="submit" class="button">Generate Rates</button>
   </p>
</form>
</div>

<div class="flex-item">
    <table>
      <thead>
        <tr>
          <th>Mortgage Term</th>
          <th>Monthly Payment</th>
          <th>Interest Rate</th>
          <th>Total Amount</th>
          <th>Total Over Loan Term</th>
          <th>Total Interest Paid</th>
        </tr>
      </thead>
      <tbody v-if="this.Loans.length">
        <tr v-for="Loan in this.Loans" :key="Loan.id">
          <td>{{ Loan.mortgage_term }}</td>
          <td>{{ Loan.monthly_payment }}</td>
          <td>{{ Loan.interest_rate }}</td>
          <td>{{ Loan.loan_amount }}</td>
          <td>{{ Loan.total_amount_paid }}</td>
          <td>{{ Loan.total_interest_paid }}</td>
        </tr>
      </tbody>
      <tbody v-else>
        <tr v-for="index in 10" :key="index">
          <td>Term in Years</td>
          <td>Payment in $</td>
          <td>Interest in %</td>
          <td>Amount in $</td>
          <td>Amount in $</td>
          <td>Amount in $</td>
        </tr>
      </tbody>
    </table>
</div>
</div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      purchasePrice: null,
      downPaymentDollar: null,
      downPaymentPercent: null,
      mortgageTerm: null,
      interestRate: null,
      Loans: [],
    };
  },
  methods: {
    createLoan() {
      axios
        .post("http://localhost:8000/calculator/loans/", {
          purchase_price: this.purchasePrice,
          down_payment_dollar: this.downPaymentDollar,
          down_payment_percent: this.downPaymentPercent,
          mortgage_term: this.mortgageTerm,
          interest_rate: this.interestRate,
        })
        .then((response) => {
          this.Loans.push(response.data);
        })
        .catch((error) => {
          console.log(error);
        });

        this.$refs.loanForm.reset();
    },
    fetchLoans() {
      axios
        .get("http://localhost:8000/calculator/loans/")
        .then((response) => {
          this.Loans = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.fetchLoans();
  },
};

</script>
<style>
div {
    font-family: Tahoma, Verdana, Segoe, sans-serif;
    padding: 5%;
    border-radius: 8px;
}
.container {
    background-color:#ccc;
    display:flex;
}
.flex-item {
    background-color:#fff;
    flex-grow: 1;
    text-align: left;
}

.flex-item:first-child {
    margin-right: 20px;
}

.button {
    background-color:#09f;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 10px 28px;
}

h1 {
    text-align: left;
    color: #038;
}

label {
    color: #038;
}
</style>
