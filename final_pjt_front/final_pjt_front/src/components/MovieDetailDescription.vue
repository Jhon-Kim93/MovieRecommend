<template>
  <div class="container p-5 backsheet">
    <div class="d-flex row">
      <div class="col-6">
        <img
          :src="'https://image.tmdb.org/t/p/w500' + selectedMovie.poster_path"
          style="width: 15rem; height: 20rem"
          class="mb-4 col-3 poster-card"
        >
        <h3 >제목: {{ selectedMovie.title }}</h3>
        <div class="row" style="height: 4rem">
          <div class="col-6 align-self-center text-content" style="text-align:right">평점: {{ selectedMovie.vote_average }}점</div>
          <div
            v-if="isRecommended"
            class="col-6 d-flex justify-content-start"
            style="height: 4rem"
          >
            <button
              class="col-4 btn btn-danger mx-3 mt-2"
              @click="addRecommend"
              style="height:3rem"
            >추천 취소</button>
          </div>
          <div
            v-else
            class="col-6 d-flex justify-content-start"
            style="height: 4rem"
          >
            <button
              class="col-4 btn btn-primary mx-3 mt-2"
              @click="addRecommend"
              style="width: 9rem; height:3rem"
            >I recommend ♥</button>
          </div>
        </div>
      </div>
      <video-app class="col-6"
        :movie='movie'
      ></video-app>
      <br>
      <hr>
      <h3>[줄거리]</h3>
      <hr style="color:black">
      <p>{{ selectedMovie.overview }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VideoApp from "@/components/youTube/VideoApp.vue"

export default {
  name: 'MovieDetailDescription',
  components: {
    VideoApp,
  },
  props: {
    movie:Array
  },
  data: function () {
    return{
      selectedMovie: this.movie[0],
      isRecommended: false,
    }
  },
  methods : {
    addRecommend: function () {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.selectedMovie.id}/recommend_users/`,
        headers: this.$store.getters.setToken
      })
        .then(res => {
          this.$store.dispatch('saveMovies')
          this.isRecommended = res.data.is_recommended
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    const username = this.$store.state.user.username
    if (this.movie[0].recommend_users) {
      const checkuser = this.movie[0].recommend_users.filter(recommend_user => {
        return recommend_user.username === username
      })
      if (checkuser[0].username === username) {
        this.isRecommended = true
      } else {
        this.isRecommended = false
      }
    }
  }
}
</script>

<style>

</style>