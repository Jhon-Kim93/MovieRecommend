<template>
  <div class="container p-5 backsheet">
      <h2>재밌으셨다면 후기를 남겨주세요!</h2>
      <router-link :to="{name:'reviewCreate', params:{movieTitle}}">
        <button class="btn btn-light">리뷰 작성하기</button>
      </router-link>
      <hr>
      <div v-if="isReviews">
        <h2>[리뷰 목록]</h2>
        <div v-for="review in reviews" :key="review.id">
          <router-link
            :to="{name:'reviewDetail', params: {reviewId: review.id}}"
            id="removeAtag" class="text-content"
          >
            <span>제목: {{review.title}} | </span>
          </router-link>
          <span class="text-content">평점: {{review.rank}}점</span>
          <br>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'MovieDetailReview',
  props: {
    movie:Array
  },
  data: function () {
    return {
      selectedMovieId: this.movie[0].id,
      movieTitle: this.movie[0].title,
      isReviews: false,
    }
  },
  computed: {
    reviews: function() {
      return this.$store.state.reviews.filter(review => {
        return review.movie.pk === this.selectedMovieId
      })
    }
  },
  created: function () {
    this.isReviews= true
  }
}
</script>

<style>

</style>