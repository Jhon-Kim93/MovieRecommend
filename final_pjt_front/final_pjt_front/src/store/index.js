import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    user: null,
    userPk: null,
    isLogin: false,
    isStaff: false,
    token: null,
    recommendShow: false,
    youtubeUrl: null,
    movies: [],
    reviews: [],
    comments: [],
  },
  mutations: {
    LOGIN: function (state, data) {
      state.isLogin = true
      state.token = localStorage.getItem('jwt')
      state.user = data
      if (data.username === 'admin') {
        state.isStaff = true
      }
    },
    LOGOUT: function (state) {
      state.isLogin = false
      state.username = null
      if (state.isStaff == true) {
        state.isStaff = false
      }
    },
    SAVE_MOVIES: function (state, movieList) {
      state.movies = movieList.data
    },
    SAVE_REVIEWS: function (state, reviews) {
      state.reviews = reviews.data
    },
    SAVE_REVIEW: function (state, review) {
      state.reviews.push(review)
    },
    UPDATE_REVIEW: function (state, review) {
      const reviewId = review.id
      const index = state.reviews.findIndex(review => {
        return review.id === reviewId
      })
      state.reviews[index] = review
    },
    DELETE_REVIEW: function (state, reviewId) {
      const index = state.reviews.findIndex(review => {
        return review.id === reviewId
      })
      state.reviews.splice(index, 1)
    },
    CREATE_COMMENT: function (state, commentData) {
      state.comments.push(commentData.data)
    },
    REVIEW_COMMENTS: function (state, Comments) {
      state.comments = Comments.data
    },
    COMMENT_UPDATE: function (state, comment) {
      const commentId = comment.id
      const index = state.comments.findIndex(comment => {
        return comment.id === commentId
      })
      state.comments[index] = comment
    },
    DELETE_COMMENT: function (state, comment) {
      const commentId = comment.id
      const index = state.comments.findIndex(comment => {
        return comment.id === commentId
      })
      state.comments.splice(index, 1)
    },
    RECOMMEND_SHOW: function (state) {
      state.recommendShow = true
    },
    RECOMMEND_UN_SHOW: function (state) {
      state.recommendShow = false
    },
    GET_YOUTUBE_URL: function (state, youtubeUrl) {
      state.youtubeUrl = youtubeUrl
    }
  },


  actions: {
    login: function ({ commit }, username) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${username}/login/`,
        data: username
      })
      .then(res => {
        commit('LOGIN', res.data)
      })
    },
    logout: function ({commit}) {
      localStorage.removeItem('jwt')
      commit('LOGOUT')
    },
    saveMovies: function ({commit}) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/index_list/',
      })
      .then(res => {
        commit('SAVE_MOVIES', res)
      })
    },
    saveReviews: function ({commit}) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/',
      })
      .then(res => {
        commit('SAVE_REVIEWS', res)
      })
    },
    saveReview: function ({commit}, review) {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/community/create/',
        data: review,
        headers: this.getters.setToken
      })
      .then( review => {
        commit('SAVE_REVIEW', review.data)
      })
    },
    updateReview: function ({commit}, review) {
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/community/${review.reviewId}/detail_update_delete`,
        data: review,
        headers: this.getters.setToken
      })
      .then( review => {
        commit('UPDATE_REVIEW', review.data)
      })
    },
    deleteReview: function ({commit}, reviewId) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/${reviewId}/detail_update_delete`,
        headers: this.getters.setToken
      })
      .then(() => {
        alert('삭제 완료')
        commit('DELETE_REVIEW', reviewId)
      })
    },
    createComment: function ({commit}, commentData) {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/community/${commentData.reviewId}/comments/create/`,
        data: commentData,
        headers: this.getters.setToken
      })
      .then(commentData => {
        commit('CREATE_COMMENT', commentData)
      })
    },
    reviewComments: function ({commit}) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/review_comments/`,
      })
      .then(comments => {
        commit('REVIEW_COMMENTS', comments)
      })
      .catch(err => {
        console.log(err)
      })
    },
    commentUpdate: function ({commit}, comment) {
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/community/${comment.reviewId}/comments/${comment.commentId}/update_delete/`,
        data: comment,
        headers: this.getters.setToken
      })
      .then(comment => {
        commit('COMMENT_UPDATE', comment.data)
      })
    },
    deleteComment: function ({commit}, comment) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/${comment.reviewId}/comments/${comment.commentId}/update_delete/`,
        headers: this.getters.setToken
      })
      .then(() => {
        commit('DELETE_COMMENT', comment.commentId)
      })
    },
    recommendShow: function ({commit}) {
      commit('RECOMMEND_SHOW')
    },
    recommendUnShow: function ({commit}) {
      commit('RECOMMEND_UN_SHOW')
    },
    getYoutubeUrl: function ({commit}, youtubeUrl) {
      commit('GET_YOUTUBE_URL', youtubeUrl)
    }
  },
  getters: {
    setToken: function (state) {
      const config = {
        Authorization : `JWT  ${state.token}`
      }
      return config
    }
  },
  modules: {
  }
})
