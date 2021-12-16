<template>
  <div class="container d-flex justify-content-center">
    <community-review-pagination></community-review-pagination>
  </div>
</template>

<script>
import CommunityReviewPagination from '../../components/paginated/CommunityReviewPagination.vue'

export default {
  components: { CommunityReviewPagination },
  name: 'community',
}
</script>

<style>

</style>