import Vue from "vue";
import VueRouter from "vue-router";

import Home from "@/views/Home.vue";
import Login from "@/views/Login";
import Maps from "@/views/Maps";
import Mypage from "@/views/Mypage";
import Otherpage from "@/views/Otherpage";
import Signup from "@/views/Signup";
import Survey from "@/views/Survey";
import ProfileUpdate from "@/views/ProfileUpdate";

import Community from "@/views/Community";
import CommunityReviewItem from "@/components/community/CommunityReviewItem";

import Heritage from "@/views/Heritage";
import HeritageCardDetail from "@/components/heritage/HeritageCardDetail";
import HeritageSearchBar from "@/components/heritage/HeritageSearchBar";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/heritage",
    name: "Heritage",
    component: Heritage,
  },
  {
    path: "/heritage/:id",
    name: "HeritageCardDetail",
    component: HeritageCardDetail,
  },
  {
    path: "/heritage/search/",
    name: "HeritageSearchBar",
    component: HeritageSearchBar,
  },
  {
    path: "/community",
    name: "Community",
    component: Community,
  },
  {
    path: "/community/:id",
    name: "CommunityReviewItem",
    component: CommunityReviewItem,
  },
  {
    path: "/maps",
    name: "Maps",
    component: Maps,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    // 로그인되어있으면 메인페이지로 보내버리기
    beforeEnter(from, to, next) {
      if (!!sessionStorage.id === true) {
        alert("로그인 된 상태에서는 할 수 없습니다")
        next('/')
      } else {
        next()
      }
    }
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
    // 로그인되어있으면 회원가입 못하게 하기
    beforeEnter(from, to, next) {
      if (!!sessionStorage.id === true) {
        alert("로그인 된 상태에서는 할 수 없습니다")
        next('/')
      } else {
        next()
      }
    }
  },
  {
    path: "/mypage",
    name: "Mypage",
    component: Mypage,
    // 로그인 안했으면 못들어가게 하기
    beforeEnter(from, to, next) {
      if (!sessionStorage.id) {
        alert("로그인이 필요합니다")
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path: "/otherpage/:nickname",
    name: "Otherpage",
    component: Otherpage,
  },
  {
    path: "/profileupdate",
    name: "ProfileUpdate",
    component: ProfileUpdate,
    // 로그인 앙ㄴ했으면 못들억어감
    beforeEnter(from, to, next) {
      if (!sessionStorage.id) {
        alert("로그인이 필요합니다")
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path: "/survey",
    name: "Survey",
    component: Survey,
    beforeEnter(from, to, next) {
      // from과 to는 컴포넌트, next는 함수다
      if (!sessionStorage.id) {
        alert("로그인이 필요합니다")
        next('/login')
      } else {
        next()
      }
    }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
