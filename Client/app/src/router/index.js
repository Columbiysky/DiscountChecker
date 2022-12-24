/* eslint-disable */
import { createRouter, createWebHistory } from 'vue-router'
import LoginPageView from '../views/LoginPageView.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginPageView
  },
  {
    path: '/main',
    name: 'main',
    component: () => import('../views/MainPageView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
