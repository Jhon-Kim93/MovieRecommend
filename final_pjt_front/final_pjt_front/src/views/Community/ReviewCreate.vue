<template>
  <div class="container d-flex justify-content-center flex-wrap backsheet p-4">
    <p class="col-12 d-flex justify-content-center text-title m-0">영화 리뷰 작성</p>
    <hr class="col-12 mb-4">
    <div class="col-6 d-flex justify-content-center flex-wrap">
      <div class="col-12 m-4 ">
        <img
          :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path"
          style="width: 35rem; height: 45rem"
        >
      </div>
      <hr class="col-12">
      <p
        class="col-12 d-flex justify-content-center text-content"
      >
      영화 제목 : {{reviewData.movie_title}}
      </p>
    </div>
    <div
      class="col-6 d-flex justify-content-start flex-wrap"
      style="height: 20rem"
    >
      <div class="col-11 offset-1 d-flex mt-4 mb-3">
        <label for="inputTitle" class="text-content ">제목 :</label> &ensp;
        <input
          type="text"
          placeholder="제목 입력"
          v-model="reviewData.title"
          id="inputTitle"
          style="align-self: flex-start;"
          maxlength="15"
          autofocus
          required
        >
      </div>
      <div class="col-11 offset-1 d-flex">
        <label for="inputRank" class="text-content">평점 :</label> &ensp;
        <input
          type="number"
          min="0"
          max="10"
          placeholder="0~10"
          v-model.number="reviewData.rank"
          id="inputRank"
          style="align-self: flex-start;"
          required
        >
      </div>
      <div class="col-11 offset-1 d-flex flex-wrap">
        <p class="text-content col-12 mt-3 mb-0">내용</p>
        <textarea
          type="text"
          placeholder="내용 입력"
          v-model="reviewData.content"
          @keyup.enter="saveReview"
          style="width: 35rem; height: 42rem; border-radius: 8px; padding:1rem; resize:none;"
          required
        >
        </textarea>
      </div>
    </div>
    <hr class="col-12" style="color:black">
    <div class="col-12">
      <button
        class="btn btn-danger"
        @click="saveReview"
        style="width: 5rem"
      >제출</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewCreate",
  data: function () {
    return {
      movie: null,

      reviewData: {
        title : null,
        movie_title: this.$route.params.movieTitle,
        rank: null,
        content: null,
      }
    }
  },
  methods: {
    saveReview: function () {
      this.$store.dispatch('saveReview', this.reviewData)
      this.$router.push({name:'community'})
    }
  },
  created: function () {
    const movies = this.$store.state.movies

    for (let movie of movies) {
      if (movie.title === this.reviewData.movie_title) {
        this.movie = movie
      }
    }
  }
}
</script>

<style>

</style>