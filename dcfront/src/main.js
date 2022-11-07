import Vue from 'vue'
import App from './App.vue'
import router from './routes.js'
// import store from './store'
import store from './store/index.js'
import IdleVue from 'idle-vue'
import 'bootstrap/dist/css/bootstrap.min.css';
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);

const eventsHub = new Vue();

Vue.use(IdleVue, {
  eventEmitter: eventsHub,
  idleTime: 900000
});

Vue.config.productionTip = false;

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requiresLogin)) {
//     if (!store.getters.loggedIn) {
//       next({ name: 'login' })
//     } else {
//       next()
//     }
//   } else {
//     next()
//   }
// });

router.beforeEach((to, from, next) => {
    const { isAuth } = store.getters;
    if (to.meta.requiresLogin) {
      if (!isAuth) {
        next ({
          path: '/login'
        })
      } else {
        next()
     }} else {
        next()
     }
});

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
