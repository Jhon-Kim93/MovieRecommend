<template>
  <div>
    <div v-if="video">
      <iframe
        :src="`${videoUrl}?autoplay=1`"
        allow='autoplay'
        width="600px" height="320px" align="right" allowfullscreen
      >
      </iframe>
    </div>
    <div v-else-if="firstvideo">
      <iframe
        :src="`${firstVideoUrl}?autoplay=1`"
        allow='autoplay' 
        width="600px" height="320px" align="right" allowfullscreen
      >
      </iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: Object,
    },
    firstvideo: {
      type: Object,
    }
  },
  computed: {
    videoUrl: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },
    firstVideoUrl: function () {
      const firstVideoId = this.firstvideo.id.videoId
      return `https://www.youtube.com/embed/${firstVideoId}`
    }
  }
}
</script>

<style>

</style>
