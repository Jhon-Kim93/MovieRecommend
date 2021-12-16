<template>
  <div class="container">
    <h3>{{username}}님이 추천한 영화</h3>
    <hr>
    <div style="display: grid; grid-template-columns:repeat(3,1fr);">
      <div
        v-for="recommendMovie in paginatedData" :key="recommendMovie.id"
        class="col-12"
        style="display: inline; height: 25rem"
      >
          <router-link :to="{name:'movieDetail', params:{movieId:recommendMovie.id}}" id="removeAtag">
            <img
              :src="'https://image.tmdb.org/t/p/w500' + recommendMovie.poster_path"
              class="mb-2 col-3"
              style="width: 13rem; height: 18.5rem"
            >
            <p class="">제목: {{ recommendMovie.title }}</p>
            <p>평점: {{ recommendMovie.vote_average }}</p>
          </router-link>
          <hr>
      </div>
    </div>
    <div class="btn-cover col-12">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ProfileRecommendMovies',
  props: {
    username: String
  },
  data: function () {
    return {
      recommendMovies: [],
      pageNum: 0,
      pageSize: 6,
    }
  },
  methods: {
    nextPage () {
      this.pageNum += 1
    },
    prevPage () {
      this.pageNum -= 1
    }
  },
  computed: {
    pageCount () {
      let listLength = this.recommendMovies.length,
          listSize = this.pageSize,
          page = Math.floor(listLength / listSize) + 1
      
      return page
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + (this.pageSize);

      return this.recommendMovies.slice(start, end)
    }
  },
  created: function () {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/${this.$route.params.username}/recommend_movies/`,
    })
    .then( res => {
      this.recommendMovies = res.data.recommend_movies
    })
    .catch(err => {
      console.log(err)
    })
  }
}
</script>

<style>

</style>