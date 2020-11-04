<template>
  <div class="community-review-item">
    <v-container>
      <v-row>
        <v-btn
          class="ma-2"
          outlined
          fab
          @click="$router.push({ name: 'Community' })"
        >
          <v-icon>mdi-format-list-bulleted-square</v-icon>
        </v-btn>
      </v-row>
      <div v-if="reviewData.users == userData.nickname">
        <v-row justify="end">
          <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                tile
                color="teal"
                dark
                v-bind="attrs"
                v-on="on"
                @click="connectReview()"
              >
                <v-icon left> mdi-pencil </v-icon>
                수정
              </v-btn>
              <v-btn tile dark @click="deleteReview(reviewData.id)">
                <v-icon left> mdi-close </v-icon>
                삭제
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <h1>리뷰 수정하기</h1>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-text-field
                    label="제목"
                    v-model="title"
                    required="제목을 입력해 주세요!"
                    autofocus
                  ></v-text-field>
                  <h3>방문한 문화재 : {{ heritageName }}</h3>
                  <v-textarea
                    label="내용"
                    v-model="content"
                    required="내용을 입력해 주세요!"
                    @keypress.enter="updateReview(reviewData.id)"
                  ></v-textarea>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="error" text @click="dialog = false">
                  <h3>닫기</h3>
                </v-btn>
                <v-btn
                  color=" darken-1"
                  text
                  @click="updateReview(reviewData.id)"
                >
                  <h3>작성완료</h3>
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-row>
      </div>
      <div class="d-flex flex-column align-center">
        <h1>{{ reviewData.title }}</h1>
        <v-img :src="reviewData.imageurl" width="30vw" class="rounded-xl" />

        <h2>방문 문화재 {{ heritageName }}</h2>
        <hr />
        <h2 @click="goOtherpage(reviewData.users)" class="review-user">
          작성자 : {{ reviewData.users }}
        </h2>
        <h3>작성날짜 : {{ reviewData.created_at }}</h3>
        <h3>{{ reviewData.content }}</h3>
      </div>
    </v-container>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import { mapState, mapGetters } from "vuex";

export default {
  name: "CommunityReviewItem",
  created() {
    this.userData.id = sessionStorage.id === undefined ? "" : sessionStorage.id;
    this.userData.nickname =
      sessionStorage.nickname === undefined ? "" : sessionStorage.nickname;
    axios
      .get(SERVER.URL + SERVER.ROUTES.review + this.$route.params.id)
      .then((res) => {
        this.reviewData = res.data;
        axios
          .get(SERVER.URL + SERVER.ROUTES.heritage + this.reviewData.heritage)
          .then((res) => (this.heritageName = res.data.k_name));
      });
  },
  computed: {
    ...mapGetters(["config"]),
    ...mapState({ review: "review" }),
  },
  methods: {
    updateReview(id) {
      const reviewUpdateData = {
        title: this.title,
        content: this.content,
        heritage: this.heritage,
        user: this.userData.id,
      };
      axios
        .put(
          SERVER.URL + SERVER.ROUTES.review + id + "/",
          reviewUpdateData,
          this.config
        )
        .then(() => {
          this.dialog = false;
          axios
            .get(SERVER.URL + SERVER.ROUTES.review + id)
            .then((res) => (this.reviewData = res.data));
        })
        .catch((err) => {
          console.error(err.message);
        });
    },
    deleteReview(id) {
      axios
        .delete(SERVER.URL + SERVER.ROUTES.review + id + "/")
        .then(() => {
          this.$router.push({ name: "Community" });
        })
        .catch((err) => {
          console.error(err.message);
        });
    },
    connectReview() {
      this.title = this.reviewData.title;
      this.content = this.reviewData.content;
      this.heritage = this.reviewData.heritage;
    },
    goOtherpage(username) {
      if (this.userData.nickname === username) {
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
      userData: {
        id: "",
        nickname: "",
      },
      reviewData: {
        content: "",
        created_at: "",
        id: "",
        title: "",
        updated_at: "",
        heritage: "",
      },
      title: "",
      content: "",
      heritage: "",
      dialog: false,
      heritageName: "",
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/community/communityReviewItem.scss";
</style>
