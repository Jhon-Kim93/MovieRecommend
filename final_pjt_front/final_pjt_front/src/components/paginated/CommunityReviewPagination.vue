<template>
  <div class="container offset-1">
    <h3>영화 리뷰</h3>
    <hr class="col-11">
    <div class="col-11">
      <div v-for="review in paginatedData" :key="review.id">
        <router-link
          :to="{name:'reviewDetail', params: {reviewId: review.id}}"
          id="removeAtag" class="text-content"
        ><h4>글 제목: {{review.title}}</h4>
        </router-link>
        <p>영화제목: {{review.movie_title}} | 작성자: {{review.user.username}} | 작성 시각: {{review.created_at}}</p>
        <hr>
      </div>
    </div>
    <div class="btn-cover">
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
import _ from "lodash"

export default {
  name:"ProfileReviewPaginated",
  data () {
    return {
      pageNum: 0,
    }
  },
  props: {
    pageSize: {
      type: Number,
      required: false,
      default: 10
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
      let listLength = this.reviews.length,
          listSize = this.pageSize,
          page = Math.floor(listLength / listSize) + 1
      
      return page
    },
    reviews: function () {
      const stateReviews = _.cloneDeep(this.$store.state.reviews)
      const showReviews = stateReviews.reverse()
      return showReviews
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + (this.pageSize - 1);

      return this.reviews.slice(start, end)
    }
  },
}
</script>

<style>
.btn-cover {
  margin-top: 1.5rem;
  text-align: center;
}
.btn-cover .page-btn {
  width: 5rem;
  height: 2rem;
  letter-spacing: 0.5px;
}
.btn-cover .page-count {
  padding: 0 1rem;
}
</style>