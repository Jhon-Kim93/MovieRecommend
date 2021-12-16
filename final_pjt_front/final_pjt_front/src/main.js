import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VModal from 'vue-js-modal'

import 'bootstrap/dist/css/bootstrap.min.css'
import '@/assets/css/main.css'
import store from './store'

Vue.use(VModal, {dynamic:true})
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')