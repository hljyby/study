import Vue from 'vue'
import App from './App.vue'
import router from './router'

import {
  messageBox
} from './components/JS'

Vue.prototype.$messageBox = messageBox

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')