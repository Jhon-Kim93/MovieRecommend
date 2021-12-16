import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Signup from '../views/Signup.vue'
import Login from '../views/Login.vue'
import Profile from '../views/Profile.vue'
import Community from '../views/Community/Community.vue'
import ReviewCreate from '../views/Community/ReviewCreate.vue'
import ReviewDetail from '../views/Community/ReviewDetail.vue'
import ReviewEdit from '../views/Community/ReviewEdit.vue'
import MovieDetail from '../views/MovieDetail'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/accounts/:username',
    name: 'profile',
    component: Profile
  },
  {
    path: '/movies/:movieId',
    name: 'movieDetail',
    component: MovieDetail
  },
  {
    path: '/community',
    name: 'community',
    component: Community
  },
  {
    path: '/community/:movieTitle',
    name: 'reviewCreate',
    component: ReviewCreate
  },
  {
    path: '/community/:reviewId',
    name: 'reviewDetail',
    component: ReviewDetail
  },
  {
    path: '/community/:reviewId/edit',
    name: 'reviewEdit',
    component: ReviewEdit
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
