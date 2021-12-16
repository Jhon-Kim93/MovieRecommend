<template>
<div class="container d-flex" v-if="isLoginUser">
    <div class="backsheet p-4 col-6 offset-3" style="text-align: left">
      <div>
        <label for="inputTitle" class="text-content p-3">글 제목 :</label> &nbsp;
        <input type="text"
          placeholder="제목 입력"
          v-model="reviewData.title"
          id="inputTitle"
          style="align-self: flex-start;"
          maxlength="15"
          autofocus
          required
        >
      </div>
      <div class="text-content p-3">영화 제목 : {{reviewData.movie_title}}</div>
      <div>
        <label for="inputRank" class="text-content p-3">평점 :</label> &nbsp;
        <input type="number"
          min="0"
          max="10"
          placeholder="0~10"
          v-model.number="reviewData.rank"
          id="inputRank"
          style="align-self: flex-start;"
          required>
      </div>
      <hr>
      <div style="display: inline-block">
        <p for="inputContent" class="text-content px-3">내용</p>
        <textarea
          type="text"
          v-model="reviewData.content"
          @keyup.enter="updateReview"
          style="width: 35rem; height: 20rem; border-radius: 8px; padding:1rem; resize:none;"
          class="mx-3"
          required
        >
        </textarea>
      </div>
      <div style="text-align: center">
        <button class="btn btn-secondary m-3" @click="updateReview">제출</button>
      </div>
    </div>
    <br>
  </div>
</template>

<script>
export default {
  name: "ReviewEdit",
  data: function () {
    return {
      reviews: this.$store.state.reviews,

      reviewData: {
        reviewId: this.$route.params.reviewId,
        title: null,
        movie_title: null,
        rank: null,
        content: null,
      },

      username: this.$store.state.user.username,
      isLoginUser: false,
    }
  },
  created: function () {
    this.reviews.filter(review => {
      if (review.id === this.reviewData.reviewId) {
        this.reviewData.title = review.title
        this.reviewData.movie_title = review.movie.title
        this.reviewData.rank = review.rank
        this.reviewData.content = review.content
        if (review.user.username === this.username) {
          this.isLoginUser = true
        }
      }
    })
  },
  methods: {
    updateReview: function () {
      this.$store.dispatch('updateReview', this.reviewData)
      this.$router.push({name:'community'})
    }
  }
}
</script>

<style>

</style>