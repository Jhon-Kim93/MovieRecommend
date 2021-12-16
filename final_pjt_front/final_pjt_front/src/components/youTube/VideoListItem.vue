<template>
  <div
    @click="selectVideo"
    class="mt-4"
  >
    <img 
      :src="video.snippet.thumbnails.default.url" 
      alt="youtube thumbnail"
    >
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
      required: true,
    }
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  }
}
</script>

<style>

</style>
