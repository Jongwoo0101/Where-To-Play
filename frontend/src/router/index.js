import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    }
  },
  {
    path: '/findplace',
    name: 'findplace',
    component: require('@/views/FindPlace.vue').default
  },
  {
    path: '/signup',
    name: 'signup',
    component: require('@/views/SignUp.vue').default
  },
  {
    path: '/login',
    name: 'login',
    component: require('@/views/Login.vue').default
  },
  {
    path: '/addplace',
    name: 'addplace',
    component: require('@/views/AddPlace.vue').default
  },
  {
    path: '/thememap',
    name: 'thememap',
    component: require('@/views/ThemeMap.vue').default
  },
  {
    path: '/adjustplace/:placeID',
    name: 'adjustplace',
    component: require('@/views/AdjustPlace.vue').default
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
