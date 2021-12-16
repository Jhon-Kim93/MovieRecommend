<template>
  <div id="videoapp">
    <section>
      <video-detail :firstvideo="firstvideo" :video="selectedVideo"></video-detail>
      <video-list :videos="videos" @select-video="onVideoSelect"></video-list>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import VideoList from '@/components/youTube/VideoList'
import VideoDetail from '@/components/youTube/VideoDetail'

export default {
  name: 'videoapp',
  components: {
    VideoList,
    VideoDetail,
  },
  props: {
    movie: Array
  },
  data: function () {
    return {
      movieTitle: null,
      videos: [],
      firstvideo: null,
      selectedVideo: null,
    }
  },
  methods: {
    onVideoSelect: function (video) {
      this.selectedVideo = video
    }
  },
  created: function () {
      // const API_KEY = 'AIzaSyC9-xOJHE43tMZrXVm_8cxmWpZCOBwAmn0'
      const API_KEY = 'AIzaSyBfQfINV5_cu70X3gCdVPg6P6O-5ZRO4-E'
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      
      this.movieTitle = this.movie[0].title + ' 예고편'

      const params = {
        key: API_KEY,
        part: 'snippet',
        q: this.movieTitle,
        type: 'video'
      }

      axios({
        method: 'get',
        url: API_URL,
        params,
      })
        .then(res => {
          for (let i=0; i<4; i++) {
            this.videos.push(res.data.items[i])
          }
          // this.videos = res.data.items
          this.firstvideo = res.data.items[0]
        })
        .catch(err => {
          console.log(err)
        })
  },
}
</script>

<style>
</style>
