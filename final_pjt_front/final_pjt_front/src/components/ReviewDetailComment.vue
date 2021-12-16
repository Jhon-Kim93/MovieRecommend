<template>
  <div class="container">
    <div class="backsheet p-4" style="text-align: left">
      <p class="text-content">댓글 작성</p>
      <textarea
        v-model="comment"
        placeholder="댓글을 입력해주세요!"
        style="width: 70rem; height: 10rem"
        @keyup.enter="createComment"
      ></textarea> &ensp;
      <span><button class="btn btn-secondary" @click="createComment">제출</button></span>
      <hr>
      <h3>댓글 목록</h3>
      <p>(댓글 수정은 내용 클릭!)</p>
      <hr>
      <div v-for="comment in reviewComments" :key="comment.id">
        <review-detail-comment-edit
          :comment="comment"
        >
        </review-detail-comment-edit>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewDetailCommentEdit from './ReviewDetailCommentEdit.vue'

export default {
  components: { ReviewDetailCommentEdit },
  props:{
    reviewId: Number
  },
  data: function () {
    return {
      comments: this.$store.state.comments,
      comment: null,
    }
  },
  computed: {
    reviewComments: function () {
      return this.comments.filter(comment => {
        return comment.review.pk === this.reviewId
      })
    }
  },
  methods: {
    createComment: function () {
      const commentData = {
        reviewId: this.reviewId,
        content: this.comment,
      }
      this.$store.dispatch('createComment', commentData)
      this.comment = null
      this.comments = this.$store.state.comments
    },
  },
}
</script>

<style>

</style>