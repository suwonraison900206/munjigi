<template>
  <div class="community-create-review">
    <v-row justify="end">
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn class="m-5" dark v-bind="attrs" v-on="on">
            <h3>리뷰쓰기</h3>
          </v-btn>
        </template>
        <v-card ref="form" lazy-validation>
          <v-card-title>
            <h1>리뷰 작성하기</h1>
          </v-card-title>
          <v-card-text>
            <v-container>
              <!-- 제목 입력란 -->
              <v-text-field
                label="제목"
                v-model="reviewData.title"
                hint="제목을 입력해주세요."
                required="제목을 입력해 주세요!"
              ></v-text-field>
              <!-- 문화재 입력란 -->
              <v-text-field
                name="input"
                label="방문한 문화재"
                append-icon="mdi-magnify"
                v-model="searchInput"
                hide-details="auto"
                hint="방문한 문화재를 검색하여 클릭해주세요."
                required="방문한 문화재를 검색하여 클릭해주세요!"
                @keyup="searchHeritage(searchInput)"
              ></v-text-field>
              <!-- 입력에 기반한 자동검색에 따른 문화재를 보여줌 -->
              <ul v-for="(heritage, idx) in searchHeritageList" :key="idx">
                <h4 class="heritage-pick" @click="pickHeritage(heritage)">
                  {{ heritage.k_name }}
                </h4>
              </ul>
              <!-- 내용 입력란 -->
              <v-textarea
                label="내용"
                v-model="reviewData.content"
                hint="내용을 입력해주세요."
                required="내용을 입력해 주세요!"
              ></v-textarea>
            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="error" text @click="closeCheck">
              <h3>닫기</h3>
            </v-btn>
            <v-btn color=" darken-1" text @click="setReview">
              <h3>작성완료</h3>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog v-model="dialog2" max-width="500px">
        <v-card>
          <v-card-title>
            <h3>작성 중인 내용이 있습니다. 닫으시겠습니까?</h3>
            <v-spacer></v-spacer>
          </v-card-title>

          <v-btn text @click="closeReview">
            <h4>네</h4>
          </v-btn>
          <v-btn text @click="dialog2 = false">
            <h4>아니요</h4>
          </v-btn>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import { mapActions } from "vuex";

export default {
  name: "CommunityCreateReview",
  methods: {
    ...mapActions(["createReview"]),
    setReview() {
      const data = {
        URL: SERVER.URL + SERVER.ROUTES.review,
        review: this.reviewData,
      };
      this.createReview(data);

      this.$emit("create-review-community");
      this.dialog = false;
    },
    closeCheck() {
      if (this.title != "" || this.content != "") {
        this.dialog2 = true;
      } else {
        this.dialog = false;
      }
    },
    closeReview() {
      this.dialog = false;
      this.dialog2 = false;
    },
    searchHeritage(searchInput) {
      const URL =
        SERVER.URL + SERVER.ROUTES.heritage + "search/?query=" + searchInput;
      axios.get(URL).then((res) => {
        this.searchHeritageList = res.data.results;
      });
    },
    pickHeritage(heritage) {
      this.searchInput = heritage.k_name;
      this.reviewData.heritage = heritage.id;
      this.searchHeritageList = [];
    },
  },
  data() {
    return {
      reviewData: {
        title: "",
        content: "",
        heritage: "",
        user: sessionStorage.getItem("id"),
      },
      searchInput: "",
      searchHeritageList: [],
      dialog: false,
      dialog2: false,
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/community/communityCreateReview.scss";
</style>

