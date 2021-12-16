<template>
  <div class="container d-flex flex-column">
    <h3 class="col-6 align-self-center" style="text-align:center">Signup</h3>

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
          >
        </div>
      </div>
    </div>

    <div class="form-group container align-self-center" style="margin:1rem">
      <div class="row justify-content-center">
        <div class="col-6">
          <label>Password Confirm</label>
          <input
            type="password"
            class="form-control form-control-lg"
            v-model="credentials.passwordConfirmation"
            @keyup.enter="signup"
          >
        </div>
      </div>
    </div>
    
    <button
      @click="signup"
      class="btn btn-secondary btn-lg btn-block col-6 align-self-center"
      style="margin:2rem"
    >Signup</button>

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
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
        .then(() => {
          this.$router.push({ name: 'Home'})
        })
        .catch(err => {
          if (err.response.data.username) {
            alert(err.response.data.username)
          } else if (err.response.data.error) {
            alert(err.response.data.error)
          } else {
            console.log('예외')
          }
          this.credentials.password = null
          this.credentials.passwordConfirmation = null
        })
    }
  }
}
</script>

<style>

</style>