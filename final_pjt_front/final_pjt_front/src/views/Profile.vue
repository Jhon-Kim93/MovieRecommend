<template>
  <div class="container">
    <div class="d-flex justify-content-between" style="margin-top:0.5rem">
      <div class="icon-bar col-2" style="width: 10rem; height: 40rem">
        <img src="@/assets/user.png" class="profile-img m-4">
        <div
          v-if="isLoginUser"
          class="container d-flex justify-content-center flex-wrap"
        >
          <h4 class="col-12 m-0" style="text-align: center;">비밀친구 수</h4>
          <hr class="col-12">
          <p class="m-0">내가 : {{user.secret_followers.length}}명</p>
          <p class="">나를 : {{user.secret_friends.length}}명</p>
        </div>
        <div v-else>
          <div v-if="isFollowed" class="mx-3 mb-4">
            <button
              @click="addSecretFriends"
              class="btn btn-danger"
            >Secret Friend</button>
          </div>
          <div v-else class="mx-3 mb-4">
            <button
              @click="addSecretFriends"
              class="btn btn-light"
            >Secret Friend</button>
          </div>
        </div>

        <div
          id="bar-line"
        ></div>
        <div class="d-flex align-items-center flex-column m-3">
          <p style="font-size:1.5rem">Menu</p>
          <div>
            <div>
              <div @click.prevent="showRecommendMovies"><a href="" id="removeAtag">- 추천 영화</a></div>
              <div @click.prevent="showReviews"><a href="" id="removeAtag">- 영화 리뷰</a></div>
            </div>
            <div v-if="isLoginUser">
              <hr>
              <div @click.prevent="showEdit" class=""><a href="" id="removeAtag">개인 정보 수정</a></div>
            </div>
          </div>
        </div>
      </div>
      <div class="d-flex align-items-start flex-column col-10">
        <div class="backsheet p-3">
          <h1>{{username}}님의 프로필</h1>
          <hr>
          <profile-recommend-movies
            v-show="isRecommendMovies"
            :username="username"
          ></profile-recommend-movies>
          <profile-review
            v-show="isReviews"
            :username="username"
          ></profile-review>
          <profile-edit v-if="isEdit"></profile-edit>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileRecommendMovies from '@/components/ProfileRecommendMovies'
import ProfileReview from '../components/ProfileReview.vue'
import ProfileEdit from '../components/ProfileEdit.vue'
import axios from 'axios'

export default {
  name:'profile',
  components: {
    ProfileRecommendMovies,
    ProfileReview,
    ProfileEdit
  },
  data: function () {
    return {
      username: this.$route.params.username,
      user: this.$store.state.user,
      
      isRecommendMovies: true,
      isReviews: false,

      isLoginUser: false,
      isEdit: false,
      isFollowed: false,
    }
  },
  computed: {

  },
  methods: {
    showRecommendMovies: function () {
      this.isRecommendMovies = true
      this.isReviews = false
      this.isEdit = false
    },
    showReviews: function () {
      this.isRecommendMovies = false
      this.isReviews = true
      this.isEdit = false
    },
    showEdit: function () {
      this.isRecommendMovies = false
      this.isReviews = false
      this.isEdit = true
    },
    addSecretFriends: function () {
      axios({
        method: 'post',
        url:`http://127.0.0.1:8000/accounts/${this.username}/secret_friend/`,
        headers: this.$store.getters.setToken
      })
      .then(res => {
        this.$store.dispatch('login', this.$store.state.user.username)
        this.isFollowed = res.data.is_followed
      })
    }
  },
  created: function () {
    if (this.$store.state.user.username === this.username) {
      this.isLoginUser = true
    }
    const SCF = this.$store.state.user.secret_friends.filter(secret_friend => {
      return this.username === secret_friend.username})
    if (SCF[0]){
      console.log(this.username, this.$store.state.user.secret_friends)
      this.isFollowed = true
    } else {
      this.isFollowed = false
    }
  }
}
</script>

<style>
.icon-bar {
background-color: #555;
position: relative; /* Fixed Sidebar (stay in place on scroll) */
/*z-index: 1;*/ /* Stay on top */
overflow-x: hidden; /* Disable horizontal scroll */
/* display: none; */
}

.profile-img {
  height: 7rem;
  width: 7rem;
}
#bar-line {
  width: 10rem;
  height: 0.4rem;
  background-color:#1f1c1c;
}
</style>