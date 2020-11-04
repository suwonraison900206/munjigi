<template>
  <div class="heritage-cards">
    <h1>{{ chooseType }} 문화재</h1>

    <v-select
      :items="searchType"
      v-model="chooseType"
      @change="changeHeritage(chooseType)"
      solo
    >
    </v-select>

    <!-- 문화재 인피티니 카드 -->
    <div class="row">
      <v-card
        class="d-inline-block my-4 mx-auto"
        v-for="(heritage, idx) in heritageList"
        :key="heritage.id"
      >
        <v-container class="v-card-container">
          <h3 @click="setHeritage(heritage)">
            {{
              heritage.k_name.length > 15
                ? heritage.k_name.slice(0, 15) + "..."
                : heritage.k_name
            }}
          </h3>
          <v-row justify="space-around">
            <v-col cols="auto">
              <v-hover v-slot:default="{ hover }">
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
              </v-hover>
            </v-col>
            <v-col cols="auto" class="text-center pl-0">
              <v-row class="flex-column ma-0 fill-height" justify="center">
                <v-col class="px-0">
                  <v-btn icon @click="like(heritage.id, idx)">
                    <span
                      v-if="heritage.like_users.find((n) => n == userDataId)"
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
                      v-if="heritage.visit_users.find((k) => k == userDataId)"
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
    </div>

    <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
      <div
        slot="no-more"
        style="color: rgb(102, 102, 102); font-size: 14px; padding: 10px 0px"
      >
        목록의 끝입니다.
      </div>
    </infinite-loading>
  </div>
</template>

<script>
import "@/assets/css/components/heritage/heritageCards.scss";
import InfiniteLoading from "vue-infinite-loading";
import SERVER from "@/api/drf";
import axios from "axios";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "CommunityCards",
  components: {
    InfiniteLoading,
  },
  mounted() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.heritage + "?page" + "=1&sort=likes/")
      .then((res) => {
        this.heritageList = res.data.results;
      });
    this.userDataId = sessionStorage.id === undefined ? "" : sessionStorage.id;
  },
  computed: {
    ...mapGetters(["config"]),
  },
  methods: {
    ...mapActions(["setHeritage"]),
    changeHeritage(currentType) {
      this.limit = 2;
      if (currentType === "인기순") {
        axios
          .get(SERVER.URL + SERVER.ROUTES.heritage + "?page" + "=1&sort=likes/")
          .then((res) => {
            this.heritageList = res.data.results;
          });
      } else {
        axios
          .get(SERVER.URL + SERVER.ROUTES.heritage + "?page" + "=1")
          .then((res) => {
            this.heritageList = res.data.results;
          });
      }
    },
    infiniteHandler($state) {
      let URL = SERVER.URL + SERVER.ROUTES.heritage + "?page=" + this.limit;
      if (this.chooseType === "인기순") {
        URL += "&sort=likes/";
      }
      axios
        .get(URL)
        .then((response) => {
          setTimeout(() => {
            if (response.data.results) {
              this.heritageList = this.heritageList.concat(
                response.data.results
              );
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
              (res) => (this.heritageList[idx].like_users = res.data.like_users)
            );
        })
        .catch(() => {
          alert("로그인 후 이용가능한 기능입니다!");
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
              (res) => (this.heritageList[idx].dib_users = res.data.dib_users)
            );
        })
        .catch(() => {
          alert("로그인 후 이용가능한 기능입니다!");
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
                (this.heritageList[idx].visit_users = res.data.visit_users)
            );
        })
        .catch(() => {
          alert("로그인 후 이용가능한 기능입니다!");
        });
    },
  },
  data() {
    return {
      heritageList: [],
      limit: 2,
      userDataId: "",
      searchType: ["인기순", "최신순"],
      chooseType: "인기순",
    };
  },
};
</script>

<style type="text/css" lang="scss">
</style>
