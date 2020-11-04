<template>
  <div class="community">
    <CommunityCreateReview @create-review-community="createReviewCommunity" />
    <CommunitySearchBar />
    <CommunityReviewList :reviewList="reviewList" />
    <div v-if="reviewList.length >= 10">
      <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
        <div
          slot="no-more"
          style="color: rgb(102, 102, 102); font-size: 14px; padding: 10px 0px"
        >
          목록의 끝입니다.
        </div>
      </infinite-loading>
    </div>
  </div>
</template>

<script>
import InfiniteLoading from "vue-infinite-loading";
import CommunitySearchBar from "@/components/community/CommunitySearchBar";
import CommunityCreateReview from "@/components/community/CommunityCreateReview";
import CommunityReviewList from "@/components/community/CommunityReviewList";
import SERVER from "@/api/drf";
import axios from "axios";

export default {
  name: "Community",
  components: {
    InfiniteLoading,
    CommunitySearchBar,
    CommunityReviewList,
    CommunityCreateReview,
  },
  created() {
    const REVIEW_LIST_URL = SERVER.URL + SERVER.ROUTES.review + "?page=1";
    axios.get(REVIEW_LIST_URL).then((response) => {
      this.reviewList = response.data.results;
    });
  },
  methods: {
    createReviewCommunity() {
      const REVIEW_LIST_URL = SERVER.URL + SERVER.ROUTES.review + "?page=1";
      axios.get(REVIEW_LIST_URL).then((res) => {
        this.reviewList = res.data.results;
      });
    },
    infiniteHandler($state) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.review + "?page=" + this.limit)
        .then((response) => {
          setTimeout(() => {
            if (response.data.results) {
              this.reviewList = this.reviewList.concat(response.data.results);
              $state.loaded();
              this.limit += 1;
              const EACH_LEN = 10;
              if (response.data.results.length / EACH_LEN < 1) {
                $state.complete();
              }
            } else {
              // 끝 지정(No more data)
              $state.complete();
            }
          }, 1000);
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  data() {
    return {
      reviewList: [],
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/views/community.scss";
</style>