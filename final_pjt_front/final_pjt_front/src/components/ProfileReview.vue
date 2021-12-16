<template>
  <div>
    <h3>{{username}}님이 쓴 게시글</h3>
    <profile-review-pagination :user-reviews="userReviews"></profile-review-pagination>
  </div>
</template>

<script>
import ProfileReviewPagination from './paginated/ProfileReviewPagination.vue'

export default {
  components: { ProfileReviewPagination },
  name:"ProfileReview",
  data: function () {
    return {
      username: this.$route.params.username
    }
  },
  computed: {
    userReviews: function () {
      return this.$store.state.reviews.filter(review => {
        return review.user.username === this.username
      })
    }
  }
}
</script>

<style>

</style>