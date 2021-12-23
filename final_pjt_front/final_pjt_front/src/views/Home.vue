<template>
  <div class="container" style="background-color:#1f1c1c">
    <div v-if='this.$store.state.isLogin' class="d-flex justify-content-center">
      <button
        class="btn btn-primary"
        v-if="!isWant"
        @click="showRecommend"
      >영화 추천 받기!</button>
      <home-recommend
        v-else
      ></home-recommend>
    </div>
    <div
      class="d-flex align-items-center flex-column bg-secondary p-5"
      v-else
    >
      <h2>로그인하고 영화 추천 받기!</h2><br>
      <router-link to="/accounts/login">
        <button class="btn-primary">go!</button>
      </router-link>
    </div>
    <home-all-genre></home-all-genre>
    
  </div>
</template>

<script>
import HomeAllGenre from '@/components/HomeAllGenre.vue'
import HomeRecommend from '@/components/HomeRecommend.vue'

export default {
  name: 'Home',
  components: {
    HomeAllGenre,
    HomeRecommend
  },
  data: function (){
    return {
      isWant: false,
    }
  },
  computed: {

  },
  created: function () {
    
  },
  methods: {
    showRecommend: function () {
      this.isWant = true
    }
  }
}
</script>
