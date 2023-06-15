<template>
  <div>
    <h1>Loan Payment Calculator</h1>
    <form @submit.prevent="createLoan">
      <label>Purchase Price:</label>
      <input type="number" v-model.number="purchasePrice" required />

      <label>Down Payment:</label>
      <input type="number" v-model.number="downPayment" required />

      <label>Mortgage Term:</label>
      <input type="number" v-model.number="mortgageTerm" required />

      <label>Interest Rate:</label>
      <input type="number" v-model.number="interestRate" required />

      <button type="submit">Calculate</button>
    </form>

    <table>
      <thead>
        <tr>
          <th>Loan ID</th>
          <th>Purchase Price</th>
          <th>Down Payment</th>
          <th>Mortgage Term</th>
          <th>Interest Rate</th>
          <th>Total Loan Amount</th>
          <th>Monthly Payment</th>
          <th>Total Amount Paid</th>
          <th>Total Interest Paid</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="Loan in Loans" :key="Loan.id">
          <td>{{ Loan.id }}</td>
          <td>{{ Loan.purchase_price }}</td>
          <td>{{ Loan.down_payment }}</td>
          <td>{{ Loan.mortgage_term }}</td>
          <td>{{ Loan.interest_rate }}</td>
          <td>{{ Loan.total_loan_amount }}</td>
          <td>{{ Loan.monthly_payment }}</td>
          <td>{{ Loan.total_amount_paid }}</td>
          <td>{{ Loan.total_interest_paid }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      purchasePrice: null,
      downPayment: null,
      mortgageTerm: null,
      interestRate: null,
      Loans: [],
    };
  },
  methods: {
    createLoan() {
      axios
        .post("Loans/", {
          purchase_price: this.purchasePrice,
          down_payment: this.downPayment,
          mortgage_term: this.mortgageTerm,
          interest_rate: this.interestRate,
        })
        .then((response) => {
          this.Loans.push(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    fetchLoans() {
      axios
        .get("Loans/")
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
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border: 1px solid black;
  padding: 8px;
}

th {
  background-color: #f2f2f2;
}

form {
  margin-bottom: 20px;
}

button {
  margin-top: 10px;
}
</style>
