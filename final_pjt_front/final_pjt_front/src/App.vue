<template>
  <div id="app">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <div class="bg" v-if="this.$store.state.recommendShow">
      <iframe
        :src="`${this.$store.state.youtubeUrl}?autoplay=1`"
        allow='autoplay'
        width="100%" height="100%"
      >
      </iframe>
    </div>

    <div id="nav" class="container">
      <router-link to="/"><img src="@/assets/logo2.png" alt="logo" class="logo"></router-link>
      <div id="nav-bar" class="row justify-content-center align-items-end mt-4">
        <div class="col-1"> </div>
        <div class="col-3">
          <router-link to="/">Home | </router-link>
          <router-link to="/community">Community</router-link>
        </div>
        <div class="col-5 ms-auto d-flex flex-row-reverse p-0">
          <span v-if="$store.state.isLogin"  style="padding-right:0.5rem">
            <a href="" @click="logout">Logout | </a>
            <router-link :to="{name:'profile', params:{username:this.$store.state.user.username}}">My profie</router-link>
          </span>
          <span v-else style="padding-right:0.5rem">
            <router-link to="/accounts/login">Login | </router-link>
            <router-link to="/accounts/signup" style="padding-right:0.5rem">Signup</router-link>
          </span>
        </div>
        <button
          v-if="$store.state.isStaff"
          @click="callData"
          class="btn btn-secondary p-2 col-2"
        >영화 정보 갱신</button>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  methods: {
    logout: function () {
      this.$store.dispatch('logout')
      this.$router.push({ name: 'Home' })
    },
    callData: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/call_data/',
        headers: this.setToken
      })
      .then(() => {
        alert('성공???')
      })
      .catch(() => {
        alert('수행 완료')
      })
    }
  },
  computed: {
    setToken: function () {
      return this.$store.getters.setToken
    }
  },
  created: function () {
    this.$store.dispatch('saveMovies')
    this.$store.dispatch('saveReviews')
    this.$store.dispatch('reviewComments')
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #ffffff;
  background-color: #1f1c1c;
  height: auto; 
  min-height: 100%;
}

#nav {
  padding: 30px;
  position: relative;
  z-index: 1;
}

#nav a {
  text-decoration: none;
  font-size: 1.5rem;
  color: #b3b3b3;
  font-weight: bold;
}

#nav a.router-link-exact-active {
  font-weight: bold;
  text-decoration: none;
  font-size: 1.5rem;
  color: #c5c5c5;
}
#nav-bar {
  padding-top : 2rem;
  padding-left: 1rem;
  padding-right: 1rem;
}

/* customed classes */
.logo {
  width: 6.5rem;
  height: 6.5rem;
  margin: 20px;
  margin-top: 0px;
  position: absolute;
}

.text-title {
  font-weight: bold;
  text-align: center;
  color: white;
  font-size: 3rem;
}

.text-subtitle {
  font-weight: bold;
  text-align: center;
  color: white;
  font-size: 1.2rem;
}

.text-content {
  text-align: left;
  color: white;
  font-size: 1.4rem;
}

.text-time {
  text-align: right;
  color: white;
  font-size: 0.8rem;
}

.backsheet {
  width: 100%;
  height: 100%;
  text-align: center;
  position: relative;
  z-index: 1;
}
.backsheet::after {
  width: 100%;
  height: 100%;
  content: "";
  background-color: #334756;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  opacity: 0.4;
}
.overflow-text {
 position: relative;
}
.overflow-text span {
  overflow: hidden;
  /* white-space: nowrap; */
  display: -webkit-box;
  -webkit-line-clamp: 5; /* 라인수 */	
  -webkit-box-orient: vertical; 
  word-wrap: break-word;
  text-overflow: ellipsis;
  position: relative;
  width: 88%;
}
.overflow-text:before {
  content: '';
  display: inline-block;
}

.darkencard {
  background-color: black;
  opacity: 0.8;
  width: 100%;
  height: 100%;
  position: absolute;
}

/* customed Ids */
#removeAtag{
  text-decoration: none;
  color: white;
}

/* video background */
.bg {
  width: 100%;
  height: 100%;
  overflow: hidden;
  margin: 0px auto;
  position: absolute;
}
video {
  width: 100%;
}
/*------------------*/
/* Layout (No Edit) */
/*------------------*/
@media(max-width:664px) {
  .bg {
    height: auto;
  }
  video {
    height: 400px;
  }
  .text p {
    font-size: 24px;
  }
}
</style>
