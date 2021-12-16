<template>
  <div>
    <p>{{ comment.user.username }}</p>
    <div v-if="isEdit">
      <textarea
        v-model="commentEdit"
        placeholder="댓글을 입력해주세요!"
        style="width: 70rem; height: 10rem"
        @keyup.enter="updateComment"
      ></textarea> &ensp;
      <span><button
        class="btn btn-secondary"
        @click="updateComment"
      >제출</button></span>
    </div>
    <div v-else>
      <p
        @click="editComment"
      >{{commentEdit}}</p>
      <button
        @click="deleteComment"
        class="btn btn-danger"
      >삭제</button>
    </div>
    <hr>
  </div>
</template>

<script>
export default {
  name: "ReviewDetailCommentEdit",
  props: {
    comment:Object
  },
  data: function () {
    return {
      commentEdit: this.comment.content,
      isEdit: false,
    }
  },
  computed: {
    commentEditData: function () {
      const Data={
        reviewId: this.comment.review.pk,
        commentId: this.comment.id,
        content: this.commentEdit
      }
      return Data
    }
  },
  methods: {
    editComment: function () {
      this.isEdit = true
    },
    updateComment: function () {
      this.$store.dispatch('commentUpdate', this.commentEditData)
      this.isEdit = false
    },
    deleteComment: function () {
      this.$store.dispatch('deleteComment', this.commentEditData)
    }
  }
}
</script>

<style>

</style>