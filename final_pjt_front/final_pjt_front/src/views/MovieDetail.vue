<template>
  <div>
    <movie-detail-description
      :movie='movie'
    ></movie-detail-description>
    <br>
    <movie-detail-review
      :movie='movie'
    ></movie-detail-review>
  </div>
</template>

<script>
import MovieDetailDescription from "@/components/MovieDetailDescription.vue"
import MovieDetailReview from "@/components/MovieDetailReview.vue"

export default {
  name: 'MovieDetail',
  components: {
    MovieDetailDescription,
    MovieDetailReview,
  },
  data: function () {
    return {
      movieId: this.$route.params.movieId,
      movies: this.$store.state.movies
    }
  },
  computed: {
    movie: function() {
      return this.movies.filter(movie => {
        return movie.id === this.movieId
      })
    }
  },
}
</script>

<style>

</style>