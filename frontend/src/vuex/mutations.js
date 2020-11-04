export default {
  SET_TOKEN(state, token) {
    state.authToken = token
  },
  SELECT_REVIEW(state, review) {
    state.review = review
  },
  SELECT_HERITAGE(state, heritage) {
    state.heritage = heritage
  },
  SET_KEYWORD(state, keyword) {
    state.selectedKeyword = keyword
  },
  SET_LATITUDE(state, latitude) {
    state.latitude = latitude
  },
  SET_LONGITUDE(state, longitude) {
    state.longitude = longitude
  }
}
