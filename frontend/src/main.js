import Vue from "vue";
import App from "./App.vue";
import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000/api/";

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
}).$mount("#app");
