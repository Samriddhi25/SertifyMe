import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vmodal from 'vue-js-modal'
import LottieAnimation from 'lottie-vuejs'

Vue.use(vmodal)
Vue.config.productionTip = false
Vue.use(LottieAnimation)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
