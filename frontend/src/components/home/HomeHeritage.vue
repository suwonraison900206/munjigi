<template>
  <div>
    <h1 class="home-recommend-text">당신을 위한 맞춤 문화재!</h1>
    <div class="row">
      <v-card
        class="d-inline-block my-4 mx-auto"
        v-for="(recommend, idx) in recommendList"
        :key="idx"
      >
        <v-container class="v-card-container">
          <h3 @click="setHeritage(recommend)">
            {{
              recommend.k_name.length > 15
                ? recommend.k_name.slice(0, 15) + "..."
                : recommend.k_name
            }}
          </h3>
          <v-row justify="space-around">
            <v-col cols="auto">
              <v-hover v-slot:default="{ hover }">
                <v-img height="200" width="200" :src="recommend.imageurl">
                  <v-expand-transition>
                    <div
                      v-if="hover"
                      class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal display-1 white--text"
                      style="height: 100%"
                      @click="setHeritage(recommend)"
                    >
                      {{ recommend.era }}
                    </div>
                  </v-expand-transition>
                </v-img>
              </v-hover>
            </v-col>
            <v-col cols="auto" class="text-center pl-0">
              <v-row class="flex-column ma-0 fill-height" justify="center">
                <v-col class="px-0">
                  <v-btn icon @click="like(recommend.id)">
                    <span
                      v-if="recommend.like_users.find((n) => n == userDataId)"
                    >
                      <v-icon color="red lighten-2">mdi-heart</v-icon>
                    </span>
                    <span v-else>
                      <v-icon>mdi-heart</v-icon>
                    </span>
                  </v-btn>
                </v-col>
                <v-col class="px-0">
                  <v-btn icon @click="dib(recommend.id)">
                    <span
                      v-if="recommend.dib_users.find((m) => m == userDataId)"
                    >
                      <v-icon color="green lighten-2">mdi-bookmark</v-icon>
                    </span>
                    <span v-else>
                      <v-icon>mdi-bookmark</v-icon>
                    </span>
                  </v-btn>
                </v-col>
                <v-col class="px-0">
                  <v-btn icon @click="visit(recommend.id)">
                    <span
                      v-if="recommend.visit_users.find((k) => k == userDataId)"
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
  </div>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/drf";
import { mapActions, mapGetters } from "vuex";
import "@/assets/css/components/heritage/heritageCards.scss";

export default {
  name: "HomeHeritage",
  props: {
    recommend: {
      type: Array,
      required: true,
    },
  },
  created() {
    this.userDataId = sessionStorage.id === undefined ? "" : sessionStorage.id;
    const URL = SERVER.URL + SERVER.ROUTES.recommend + sessionStorage.id;
    axios
      .get(URL)
      .then((res) => {
        this.recommendList = res.data;
      })
      .catch((err) => console.error(err));
  },
  computed: {
    ...mapGetters(["config"]),
  },
  methods: {
    ...mapActions(["setHeritage"]),
    like(id) {
      axios
        .post(
          SERVER.URL + SERVER.ROUTES.heritage + id + "/like/",
          {
            userDataId: this.userDataId,
          },
          null
        )
        .then(() => {
          const URL = SERVER.URL + SERVER.ROUTES.recommend + sessionStorage.id;
          axios
            .get(URL)
            .then((res) => {
              this.recommendList = res.data;
            })
            .catch((err) => console.error(err));
        })
        .catch(() => {
          alert("로그인 후 이용가능한 기능입니다!");
        });
    },
    dib(id) {
      axios
        .post(
          SERVER.URL + SERVER.ROUTES.heritage + id + "/dib/",
          {
            userDataId: this.userDataId,
          },
          null
        )
        .then(() => {
          const URL = SERVER.URL + SERVER.ROUTES.recommend + sessionStorage.id;
          axios
            .get(URL)
            .then((res) => {
              this.recommendList = res.data;
            })
            .catch((err) => console.error(err));
        })
        .catch(() => {
          alert("로그인 후 이용가능한 기능입니다!");
        });
    },
    visit(id) {
      axios
        .post(
          SERVER.URL + SERVER.ROUTES.heritage + id + "/visit/",
          {
            userDataId: this.userDataId,
          },
          null
        )
        .then(() => {
          const URL = SERVER.URL + SERVER.ROUTES.recommend + sessionStorage.id;
          axios
            .get(URL)
            .then((res) => {
              this.recommendList = res.data;
            })
            .catch((err) => console.error(err));
        })
        .catch(() => {
          alert("로그인 후 이용가능한 기능입니다!");
        });
    },
  },
  data() {
    return {
      recommendList: [],
      userDataId: "",
    };
  },
};
</script>

<style></style>
