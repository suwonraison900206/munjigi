<template>
  <div>
    <h2>문화재 리뷰 작성 목록</h2>
    <div v-if="isEmpty">
      아직 등록된 리뷰가 없습니다.
      <div>
        <v-btn @click="$router.push({ name: 'Community' })">
          게시판으로 가기
        </v-btn>
      </div>
    </div>

    <div v-else>
      <ul v-for="(review, i) in reviewData" :key="i">
        <div @click="setReview(review)">
          <h3 class="review-pick">{{ review.title }}</h3>
          {{ review.created_at }}
        </div>
      </ul>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import { mapActions } from "vuex";

export default {
  name: "MypageReview",
  created() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.mypage + sessionStorage.nickname + "/")
      .then((res) => {
        this.reviewData = res.data.user.user_review;
        if (this.reviewData.length) {
          this.isEmpty = false;
        } else {
          this.isEmpty = true;
        }
      })
      .catch((err) => console.error(err));
  },
  methods: {
    ...mapActions(["setReview"]),
  },
  data() {
    return {
      reviewData: "",
      isEmpty: true,
    };
  },
};
</script>


<style type="text/css" lang="scss">
@import "@/assets/css/components/mypage/mypageReview.scss";
</style>

