<template>
  <div>
    <h2>리뷰 목록</h2>
    <div v-if="authToken">
      <HeritageCreateReview @create-review="createReview" />
    </div>
    <v-row justify="center" no-gutters>
      <v-col lg="3"><h3>작성자</h3></v-col>
      <v-col lg="3">
        <h3>리뷰</h3>
      </v-col>
    </v-row>
    <div v-for="review in heritageReviewList" :key="review.id">
      <v-row justify="center" no-gutters>
        <v-col lg="3" @click="goOtherpage(review.users)" class="review-user">
          {{ review.users }}</v-col
        >
        <v-col lg="3">
          <div class="pa-2" outlined tile>
            <h4>{{ review.title }}</h4>
            <h5>{{ review.content }}</h5>
            <small>{{ review.created_at }}</small>
          </div>
        </v-col>
      </v-row>
    </div>
    <div v-if="!heritageReviewList.length">
      <h5>관련 리뷰가 없습니다.</h5>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import { mapState } from "vuex";
import HeritageCreateReview from "@/components/heritage/HeritageCreateReview";

export default {
  name: "HeritageCardDetailReview",
  components: {
    HeritageCreateReview,
  },
  created() {
    this.myNickname =
      sessionStorage.nickname === undefined ? "" : sessionStorage.nickname;
    const heritageId = this.$route.params.id;
    axios
      .get(SERVER.URL + SERVER.ROUTES.heritage + heritageId)
      .then((res) => (this.heritageReviewList = res.data.heritage_reviews));
  },
  computed: {
    ...mapState(["authToken"]),
  },
  methods: {
    createReview() {
      const heritageId = this.$route.params.id;
      const REVIEW_LIST_URL = SERVER.URL + SERVER.ROUTES.heritage + heritageId;
      axios.get(REVIEW_LIST_URL).then((res) => {
        this.heritageReviewList = res.data.heritage_reviews;
      });
    },
    goOtherpage(username) {
      if (this.myNickname === username) {
        this.$router.push({ name: "Mypage" });
      } else {
        this.$router.push({
          name: "Otherpage",
          params: { nickname: username },
        });
      }
    },
  },
  data() {
    return {
      heritageReviewList: "",
      myNickname: "",
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/heritage/heritageCardDetailReview.scss";
</style>
