<template>
<div>
  <router-link :to="{name:'movieDetail', params:{movieId:movie.id}}">
    <div
      class="card text-white m-4"
      @mouseenter="active"
      @mouseleave="active"
    >
      <img
        :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path"
        class="card-img"
      >
      <div
        :class="{darkencard: isActive}">
      </div>
      <div
        class="card-img-overlay overflow-text"
        v-show="isActive"
      >
        <h5>{{ movie.title }}</h5>
        <hr>
        [줄거리]
        <span>{{ movie.overview }}</span>
        <br>
        <p>평점 : {{ movie.vote_average }}</p>
        <p>개봉일 : {{ movie.release_date }}</p>
      </div>
    </div>
  </router-link>
</div>
</template>

<script>
export default {
  name:'HomeAllGenreMovieCard',
  props: {
    movie:Object
  },
  data: function () {
    return {
      isActive: false,
    }
  },
  methods: {
    active: function () {
      this.isActive = !this.isActive
    }
  }
}
</script>

<style>

</style>