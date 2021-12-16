<template>
  <div id="home-recommend" class="container d-flex align-items-start flex-column">
    <h3 class="align-self-center">영화 추천</h3>
    <div
      class="container d-flex flex-column justify-content-center flex-wrap backsheet"
      style="height: 30em"
      v-if="!isRecommendMovies"
    >
      <h3 class="align-self-center">추천 영화가 없어요!</h3>
      <br>
      <h4 class="align-self-center">나만의 비밀 친구를 추가하고 영화를 추천받으세요!!!</h4>
      <br>
      <span>리뷰 보러 가기!</span> &ensp; <router-link :to="{name: 'community'}"><button class="btn btn-primary">go!</button></router-link>
    </div>
    <div
      v-else
      class="container box d-flex justify-content-center"
      @mouseover="recommendShow"
      @mouseout="recommendUnShow"
      
    >
      <router-link :to="{name:'movieDetail', params:{movieId:recommendMovie[0].id}}">
        <img
        :src="'https://image.tmdb.org/t/p/w500' + recommendMovie[0].poster_path"
        class="poster align-self-center select-img"
        @click="recommendUnShow"
        >
      </router-link>
      <transition name="fade">
        <div class="description ml-5" v-show="this.$store.state.recommendShow">
          <h3>제목: {{ recommendMovie[0].title }}</h3>
          <h4>평점: {{ recommendMovie[0].vote_average }}점</h4>
          <br>
          <p>[줄거리]</p>
          <p>{{ recommendMovie[0].overview }}</p>
        </div>
      </transition>
    </div>
    <div class="d-flex justify-content-center col-12">
      <button
        v-if="isRecommendMovies"
        class="btn btn-secondary"
        @click="randomMovie"
      >다른거 없어?</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'HomeRecommend',
  components: {
  },
  data: function () {
    return {
      show: false,
      recommendMovies: [],
      recommendMovie: null,
      isRecommendMovies: false,
      
      // youtube data
      searchedName: null,
    }
  },
  methods: {
    randomMovie: function() {
      this.recommendMovie = _.sampleSize(this.recommendMovies, 1)
      
      // const API_KEY = 'AIzaSyC9-xOJHE43tMZrXVm_8cxmWpZCOBwAmn0'
      const API_KEY = 'AIzaSyBfQfINV5_cu70X3gCdVPg6P6O-5ZRO4-E'
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      
      this.searchedName = this.recommendMovie[0].title + ' 예고편'

      const params = {
        key: API_KEY,
        part: 'snippet',
        q: this.searchedName,
        type: 'video'
      }

      axios({
        method: 'get',
        url: API_URL,
        params,
      })
      .then(res => {
        const backgroundVideoId = res.data.items[0].id.videoId
        const backgroundVideoUrl = `https://www.youtube.com/embed/${backgroundVideoId}`
        this.$store.dispatch('getYoutubeUrl', backgroundVideoUrl)
      })
      .catch(err => {
        console.log(err)
      })
    },
    recommendShow: function () {
      this.$store.dispatch('recommendShow')
    },
    recommendUnShow: function () {
      this.$store.dispatch('recommendUnShow')
    },
  },
  created: function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/accounts/random_recommend_movies/',
      headers: this.$store.getters.setToken
    })
    .then(res => {
      if (res.data[0]) {
        this.recommendMovies = res.data
        this.randomMovie()
        this.isRecommendMovies = true
      } else {
        this.isRecommendMovies = false
      }
    })
  }
}
</script>

<style>
#home-recommend{
  position: relative;
  z-index: 1;
}

.poster {
  width: 25rem;
  height: 37rem;
  box-shadow: 5px 5px black;
  border-radius: 9px;
  margin: 3rem;
  margin-top: 1rem;
}
.poster-card {
  width: 80rem;
  height: 37rem;
  box-shadow: 5px 5px black;
  border-radius: 9px;
  margin: 3rem;
  margin-top: 1rem;
}
.box {
  position: relative;
}
.select-img {
  /* position: absolute; */
  top:0;
  left:0;
}
.description {
  position: absolute;
  top:5rem;
  left:56%;
}

.box:hover .select-img{transform: translateX(-13rem);} 
.select-img{transform: translateX(0rem); transition: all 0.8s ease;}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /*.fade-leave-active below version 2.1.8*/{
  opacity: 0;
}
</style>