import axios from "axios";
import router from "@/routes";
import SERVER from "@/api/drf";

export default {
  postAuthData({ commit }, info) {
    axios
      .post(info.location, info.data)
      .then((res) => {
        console.log(res.data);
        commit("SET_TOKEN", res.data.token);
        // sessionStorage에 유저의 정보를 저장
        sessionStorage.setItem("auth-token", res.data.token);
        sessionStorage.setItem("birth", res.data.user.birth);
        sessionStorage.setItem("dateJoined", res.data.user.date_joined);
        sessionStorage.setItem("email", res.data.user.email);
        sessionStorage.setItem("id", res.data.user.id);
        sessionStorage.setItem("name", res.data.user.name);
        sessionStorage.setItem("nickname", res.data.user.nickname);
        sessionStorage.setItem("survey", res.data.user.survey);

        const validator = /register/;
        let location = validator.test(info.location) ? "Survey" : "Home";
        router.push({ name: `${location}` });
      })
      .catch(() => alert("이메일 또는 비밀번호가 틀렸습니다"));
  },
  signup({ dispatch }, signupData) {
    const info = {
      location: SERVER.URL + SERVER.ROUTES.signup,
      data: signupData,
    };
    dispatch("postAuthData", info);
  },
  login({ dispatch }, loginData) {
    const info = {
      location: SERVER.URL + SERVER.ROUTES.login,
      data: loginData,
    };
    !loginData.email || !loginData.password
      ? alert("이메일 또는 비밀번호를 입력해주세요")
      : dispatch("postAuthData", info);
  },
  logout({ getters, commit }) {
    axios
      .post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
      .then(() => {
        commit("SET_TOKEN", null);
        // 세션에 있는 정보를 지움
        sessionStorage.removeItem("auth-token");
        sessionStorage.removeItem("birth");
        sessionStorage.removeItem("dateJoined");
        sessionStorage.removeItem("email");
        sessionStorage.removeItem("id");
        sessionStorage.removeItem("name");
        sessionStorage.removeItem("nickname");
        sessionStorage.removeItem("survey");
      })
      .catch((err) => {
        console.log(err.message);
      });
  },
  setHeritage({ commit }, heritage) {
    commit("SET_HERITAGE", heritage);
    router.push({ name: "HeritageCardDetail", params: { id: heritage.id } });
  },
  setReview({ commit }, review) {
    commit("SET_REVIEW", review);
    router.push({ name: "CommunityReviewItem", params: { id: review.id } });
  },
  createReview({ getters }, data) {
    const config = getters.config;
    const URL = data.URL;
    const review = data.review;
    axios
      .post(URL, review, config)
      .then((res) => console.log(res))
      .catch((err) => console.error(err));
  },
};
