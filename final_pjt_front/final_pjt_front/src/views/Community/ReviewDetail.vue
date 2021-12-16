<template>
  <div class="container">
    <div class="backsheet p-4 " style="text-align: left">
      <span class="text-content">글쓴이: </span>
      <router-link
        id="removeAtag"
        :to="{name: 'profile', params:{username:review.user.username}}"
      >
        <span class="text-content">{{review.user.username}}</span>
      </router-link>
      <p class="text-content mt-3">글 제목: {{review.title}}</p>
      <p class="text-content">영화제목: {{review.movie_title}}</p>
      <p class="text-content">평점: {{review.rank}}점</p>
      <hr>
      <p class="text-content">{{review.content}}</p>
      <hr>
      <div style="text-align: right" v-if="isLoginUser">
        <router-link
          :to="{name:'reviewEdit', params:{reviewId:review.id}}"
        >
          <button class="btn btn-secondary">수정</button>
        </router-link>
        <span style="font-size:1rem"> | </span>
        <button class="btn btn-danger" @click="deleteReview">삭제</button>
      </div>
    </div>
    <div style="text-align: right">작성일: {{review.created_at}}</div>
    <br>
    <review-detail-comment
      :review-id="reviewId"
    ></review-detail-comment>
  </div>
</template>

<script>
import ReviewDetailComment from '@/components/ReviewDetailComment.vue'

export default {
  name: 'CommunityReviewDetail',
  components: {
    ReviewDetailComment
  },
  data: function () {
    return {
      reviews: this.$store.state.reviews, 
      reviewId: this.$route.params.reviewId,

      username: this.$store.state.user.username,
      isLoginUser: false,
    }
  },
  computed: {
    review: function () {
      const review = this.reviews.filter(review => {
        return review.id === this.reviewId
      })
       return review[0]
    }
  },
  methods: {
    deleteReview: function () {
      this.$store.dispatch('deleteReview', this.reviewId)
      this.$router.push({name:'community'})
    }
  },
  created: function () {
    if (this.username === this.review.user.username) {
      this.isLoginUser = true
    }
  }
}
</script>

<style>

</style>