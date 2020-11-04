<template>
  <div class="heritage-search-bar">
    <h1>문화재 검색</h1>
    <v-text-field
      class="search-input"
      name="input"
      label="찾고자 하는 문화재를 검색해 보세요!"
      append-icon="mdi-magnify"
      :rules="rules"
      v-model="searchInput"
      hide-details="auto"
      @keyup="searchHeritage(searchInput)"
    ></v-text-field>
    <div class="row">
      <ul v-for="(heritage, idx) in searchHeritageList" :key="heritage.id">
        <v-hover v-slot:default="{ hover }">
          <v-card class="d-inline-block mx-auto">
            <v-container>
              <h3 @click="setHeritage(heritage)">{{ heritage.k_name }}</h3>
              <v-row justify="space-between">
                <v-col cols="auto">
                  <v-img height="200" width="200" :src="heritage.imageurl">
                    <v-expand-transition>
                      <div
                        v-if="hover"
                        class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal display-1 white--text"
                        style="height: 100%"
                        @click="setHeritage(heritage)"
                      >
                        {{ heritage.era }}
                      </div>
                    </v-expand-transition>
                  </v-img>
                </v-col>
                <v-col cols="auto" class="text-center pl-0">
                  <v-row class="flex-column ma-0 fill-height" justify="center">
                    <v-col class="px-0">
                      <v-btn icon @click="like(heritage.id, idx)">
                        <span
                          v-if="
                            heritage.like_users.find((n) => n == userDataId)
                          "
                        >
                          <v-icon color="red lighten-2">mdi-heart</v-icon>
                        </span>
                        <span v-else>
                          <v-icon>mdi-heart</v-icon>
                        </span>
                      </v-btn>
                    </v-col>
                    <v-col class="px-0">
                      <v-btn icon @click="dib(heritage.id, idx)">
                        <span
                          v-if="heritage.dib_users.find((m) => m == userDataId)"
                        >
                          <v-icon color="green lighten-2">mdi-bookmark</v-icon>
                        </span>
                        <span v-else>
                          <v-icon>mdi-bookmark</v-icon>
                        </span>
                      </v-btn>
                    </v-col>
                    <v-col class="px-0">
                      <v-btn icon @click="visit(heritage.id, idx)">
                        <span
                          v-if="
                            heritage.visit_users.find((k) => k == userDataId)
                          "
                        >
                          <v-icon color="blue lighten-2"
                            >mdi-checkbox-marked-circle</v-icon
                          >
                        </span>
                        <span v-else>
                          <v-icon>mdi-checkbox-marked-circle</v-icon>
                        </span>
                      </v-btn>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-hover>
      </ul>
    </div>
  </div>
</template>

<script>
import "@/assets/css/components/heritage/heritageSearchBar.scss";
import SERVER from "@/api/drf";
import axios from "axios";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "CommunitySearchBar",
  mounted() {
    this.userDataId = sessionStorage.id === undefined ? "" : sessionStorage.id;
  },
  computed: {
    ...mapGetters(["config"]),
  },
  methods: {
    ...mapActions(["setHeritage"]),
    like(id, idx) {
      axios
        .post(
          SERVER.URL + SERVER.ROUTES.heritage + id + "/like/",
          {
            userDataId: this.userDataId,
          },
          null
        )
        .then(() => {
          axios
            .get(SERVER.URL + SERVER.ROUTES.heritage + id)
            .then(
              (res) =>
                (this.searchHeritageList[idx].like_users = res.data.like_users)
            );
        })
        .catch((err) => {
          console.error(err);
        });
    },
    dib(id, idx) {
      axios
        .post(
          SERVER.URL + SERVER.ROUTES.heritage + id + "/dib/",
          {
            userDataId: this.userDataId,
          },
          null
        )
        .then(() => {
          axios
            .get(SERVER.URL + SERVER.ROUTES.heritage + id)
            .then(
              (res) =>
                (this.searchHeritageList[idx].dib_users = res.data.dib_users)
            );
        })
        .catch((err) => {
          console.error(err);
        });
    },
    visit(id, idx) {
      axios
        .post(
          SERVER.URL + SERVER.ROUTES.heritage + id + "/visit/",
          {
            userDataId: this.userDataId,
          },
          null
        )
        .then(() => {
          axios
            .get(SERVER.URL + SERVER.ROUTES.heritage + id)
            .then(
              (res) =>
                (this.searchHeritageList[idx].visit_users =
                  res.data.visit_users)
            );
        })
        .catch(() => {
          alert("로그인 후 이용가능한 기능입니다!");
        });
    },
    searchHeritage(searchInput) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.heritage + "?query=" + searchInput)
        .then((res) => {
          this.searchHeritageList = res.data.results;
        });
    },
  },
  data() {
    return {
      searchInput: "",
      searchHeritageList: [],
      rules: [(value) => !!value || "한 글자 이상 입력하셔야 합니다."],
      limit: 2,
      userDataId: "",
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/heritage/heritageSearchBar.scss";
</style>