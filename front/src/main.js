import Vue from "vue"
import App from "./App.vue"
import vuetify from "./plugins/vuetify";
import router from "@/routes";
import auth from "./utils/auth"
import http from "./utils/http"
import message from "./utils/message"
import loading from "./utils/loading"

Vue.prototype.$auth = auth
Vue.prototype.$http = http
Vue.prototype.$message = message
Vue.prototype.$loading = loading


new Vue({
  vuetify,
  render: h => h(App),
  router: router
}).$mount("#app")
