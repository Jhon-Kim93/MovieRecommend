<template>
  <div>
    <div v-for="userReview in paginatedData" :key="userReview.id">
      <p class="text-content">
        <router-link
          :to="{name:'reviewDetail', params:{reviewId:userReview.id}}"
          id="removeAtag"
        >
          글 제목 : {{userReview.title}} | 
          영화 제목 : {{userReview.movie_title}} | 
          평점 : {{userReview.rank}}
        </router-link>
      </p>
      <p class="text-time">
        작성 일시 : {{userReview.created_at}}
      </p>
      <hr>
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
export default {
  name:"ProfileReviewPagination",
  data () {
    return {
      pageNum: 0
    }
  },
  props: {
    userReviews: {
      type: Array,
      required: true
    },
    pageSize: {
      type: Number,
      required: false,
      default: 8
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
      let listLength = this.userReviews.length,
          listSize = this.pageSize,
          page = Math.floor(listLength / listSize) + 1
      
      return page
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + (this.pageSize - 1);

      return this.userReviews.slice(start, end)
    }
  }
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