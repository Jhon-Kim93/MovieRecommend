<template>
  <div class="container d-flex flex-column">
    <h3 class="col-6 align-self-center" style="text-align:center">Login</h3>

    <div class="form-group container align-self-center" style="margin:1rem">
      <div class="row justify-content-center">
        <div class="col-6">
          <label>username: </label>
          <input
            type="text"
            class="form-control form-control-lg"
            v-model="credentials.username"
          >
        </div>
      </div>
    </div>

    <div class="form-group container align-self-center" style="margin:1rem">
      <div class="row justify-content-center">
        <div class="col-6">
          <label>Password</label>
          <input
            type="password"
            class="form-control form-control-lg"
            v-model="credentials.password"
            @keyup.enter="login"
          >
        </div>
      </div>
    </div>
    
    <button
      @click="login"
      class="btn btn-secondary btn-lg btn-block col-6 align-self-center"
      style="margin:2rem"
    >Login</button>

    <div class="container align-self-center" style="margin-bottom:2rem">
      <div class="row justify-content-center">
        <span class="col-2" style="text-align:center">
          <a href="#">
            <i class="fa fa-google fa-2x"></i>
          </a>
        </span>
        <span class="col-2" style="text-align:center">
          <a href="#">
            <i class="fa fa-facebook fa-2x"></i>
          </a>
        </span>
        <span class="col-2" style="text-align:center">
          <a href="#">
            <i class="fa fa-twitter fa-2x"></i>
          </a>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api/token/',
        data: this.credentials,
      })
        .then(res => {
          localStorage.setItem('jwt', res.data.token)
          this.$store.dispatch('login', this.credentials.username)
          this.$router.push({ name: 'Home' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>