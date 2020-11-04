<template>
  <div class="community-review-list">
    <h1>문화재 방문 리뷰 게시판</h1>
    <div v-for="(review, idx) in reviewList" :key="idx">
      <v-card class="review-list" outlined @click="setReview(review)">
        <v-list-item class="d-flex justify-space-around review-list-item">
          <v-img class="review-list-image" :src="review.imageurl"></v-img>
          <div class="review-list-text">
            <h3 class="mb-4">{{ review.title }}</h3>
            <h4>문화재명 : {{ review.k_name }}</h4>
            <v-list-item-subtitle
              >작성자 : {{ review.users }}</v-list-item-subtitle
            >
            <v-list-item-subtitle>{{ review.created_at }}</v-list-item-subtitle>
          </div>
        </v-list-item>
      </v-card>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "CommunityReviewList",
  props: {
    reviewList: {
      type: Array,
      required: true,
    },
  },
  methods: {
    ...mapActions(["setReview"]),
  },
  data() {
    return {
      limit: 2,
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/community/communityReviewList.scss";
</style>
