export default {
  authToken:
    sessionStorage.getItem("auth-token") === "undefined"
      ? null
      : sessionStorage.getItem("auth-token"),
  selectedKeyword: "미추홀구",
  review: {
    type: Object,
  },
  heritage: {
    type: Object,
  },
  latitude: 0,
  longitude: 0
};
