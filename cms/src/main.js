import Vue from 'vue';
import App from './App.vue';
import VCurrencyField from 'v-currency-field';
import { VTextField } from 'vuetify/lib'
import vuetify from './plugins/vuetify';
import router from "./routes";
import auth from "@/utils/auth";
import loading from "@/utils/loading";
import message from "@/utils/message";
import message_box from "@/utils/message_box";
import http from "@/utils/http";

// In order to use v-currency-field package
Vue.component('v-text-field', VTextField)
Vue.use(VCurrencyField, {
  locale: 'en',
  decimalLength: 2,
  autoDecimalMode: true,
  min: null,
  max: null,
  defaultValue: 0,
  valueAsInteger: false,
  allowNegative: false
});

Vue.config.productionTip = false
Vue.prototype.$auth = auth
Vue.prototype.$message = message
Vue.prototype.$loading = loading
Vue.prototype.$message_box = message_box
Vue.prototype.$http = http

new Vue({
  vuetify,
  render: h => h(App),
  router: router,
}).$mount('#app')


