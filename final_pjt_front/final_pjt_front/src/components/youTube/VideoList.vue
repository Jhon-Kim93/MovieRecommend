<template>
  <div class="row">
    <video-list-item 
      v-for="video in videos" 
      :key="video.id.videoId"
      :video="video"
      @select-video="onSelectVideo"
      class="col-3"
    >
    </video-list-item>
  </div>
</template>

<script>
import VideoListItem from '@/components/youTube/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
      required: true,
    }
  },
  methods: {
    onSelectVideo: function (video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>
