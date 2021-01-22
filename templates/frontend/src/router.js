import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Create from './views/Create.vue'
import Template from './views/Template.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/create',
      name: 'create',
      component: Create,
      props: true,
    },
    {
      path: '/template',
      name: 'template',
      component: Template
    },
  ]
})

// {
//   path: '/about',
//   name: 'about',
// route level code-splitting
// this generates a separate chunk (about.[hash].js) for this route
// which is lazy-loaded when the route is visited.
//   component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
// },