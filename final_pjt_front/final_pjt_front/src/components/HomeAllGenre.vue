<template>
  <div class="container" style="margin-top:3rem">
    <div class="row">
      <home-all-genre-movie-card
        class="col-4"
        v-for="movie in list" :key="movie.id" 
        :movie='movie'
      >
      </home-all-genre-movie-card>
    </div>
    <infinite-loading @infinite="infiniteHandler"></infinite-loading>
  </div>
</template>

<script>
import HomeAllGenreMovieCard from './HomeAllGenreMovieCard.vue'
import InfiniteLoading from 'vue-infinite-loading';
import axios from 'axios';

const api = 'http://127.0.0.1:8000/movies/index_list';

export default {
  name: "HomeAllGenre",
  components: {
    HomeAllGenreMovieCard,
    InfiniteLoading,
  },
  data: function () {
    return{
      page: 1,
      list: [],
      index: -1,
    }
  },
  methods: {
    infiniteHandler($state) {
      axios.get(api, {
        params: {
          page: this.page,
        },
      }).then(({ data }) => {
        if (data) {
          this.page += 1;
          this.index += 9;
          for (let i = 8; i >= 0; i--) {
            this.list.push(data[this.index - i])
          }
          $state.loaded()
        } else {
          $state.complete()
        }
      })
    },
  },
}
</script>

<style>

</style>