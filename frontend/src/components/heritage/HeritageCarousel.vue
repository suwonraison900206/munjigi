<template>
  <div class="heritage-carousel">
    <h1>추천 문화재!</h1>
    <VueSlickCarousel v-bind="settings">
      <v-card
        :loading="loading"
        class="mx-auto my-12"
        max-width="374"
        @click="setHeritage(heritageList[0])"
      >
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>
        <v-img height="200" :src="heritageList[0].imageurl"></v-img>
        <v-card-title
          ><h5>{{ heritageList[0].k_name }}</h5>
        </v-card-title>
      </v-card>
      <v-card
        :loading="loading"
        class="mx-auto my-12"
        max-width="374"
        @click="setHeritage(heritageList[1])"
      >
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>
        <v-img height="200" :src="heritageList[1].imageurl"></v-img>
        <v-card-title
          ><h5>{{ heritageList[1].k_name }}</h5>
        </v-card-title>
      </v-card>
      <v-card
        :loading="loading"
        class="mx-auto my-12"
        max-width="374"
        @click="setHeritage(heritageList[2])"
      >
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>
        <v-img height="200" :src="heritageList[2].imageurl"></v-img>
        <v-card-title
          ><h5>{{ heritageList[2].k_name }}</h5>
        </v-card-title>
      </v-card>
      <v-card
        :loading="loading"
        class="mx-auto my-12"
        max-width="374"
        @click="setHeritage(heritageList[3])"
      >
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>
        <v-img height="200" :src="heritageList[3].imageurl"></v-img>
        <v-card-title
          ><h5>{{ heritageList[3].k_name }}</h5>
        </v-card-title>
      </v-card>
      <v-card
        :loading="loading"
        class="mx-auto my-12"
        max-width="374"
        @click="setHeritage(heritageList[4])"
      >
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>
        <v-img height="200" :src="heritageList[4].imageurl"></v-img>
        <v-card-title
          ><h5>{{ heritageList[4].k_name }}</h5>
        </v-card-title>
      </v-card>
      <v-card
        :loading="loading"
        class="mx-auto my-12"
        max-width="374"
        @click="setHeritage(heritageList[5])"
      >
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>
        <v-img height="200" :src="heritageList[5].imageurl"></v-img>
        <v-card-title
          ><h5>{{ heritageList[5].k_name }}</h5>
        </v-card-title>
      </v-card>
      <v-card
        :loading="loading"
        class="mx-auto my-12"
        max-width="374"
        @click="setHeritage(heritageList[6])"
      >
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>
        <v-img height="200" :src="heritageList[6].imageurl"></v-img>
        <v-card-title
          ><h5>{{ heritageList[6].k_name }}</h5>
        </v-card-title>
      </v-card>
      <v-card
        :loading="loading"
        class="mx-auto my-12"
        max-width="374"
        @click="setHeritage(heritageList[7])"
      >
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>
        <v-img height="200" :src="heritageList[7].imageurl"></v-img>
        <v-card-title
          ><h5>{{ heritageList[7].k_name }}</h5>
        </v-card-title>
      </v-card>
      <v-card
        :loading="loading"
        class="mx-auto my-12"
        max-width="374"
        @click="setHeritage(heritageList[8])"
      >
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>
        <v-img height="200" :src="heritageList[8].imageurl"></v-img>
        <v-card-title
          ><h5>{{ heritageList[8].k_name }}</h5>
        </v-card-title>
      </v-card>
      <v-card
        :loading="loading"
        class="mx-auto my-12"
        max-width="374"
        @click="setHeritage(heritageList[9])"
      >
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>
        <v-img height="200" :src="heritageList[9].imageurl"></v-img>
        <v-card-title
          ><h5>{{ heritageList[9].k_name }}</h5>
        </v-card-title>
      </v-card>
    </VueSlickCarousel>
  </div>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import { mapActions, mapGetters } from "vuex";
import SERVER from "@/api/drf";
import axios from "axios";

export default {
  name: "CommunityCarousel",
  components: {
    VueSlickCarousel,
  },
  created() {
    this.userDataId = sessionStorage.id === undefined ? "" : sessionStorage.id;
    const URL = SERVER.URL + SERVER.ROUTES.recommend + sessionStorage.id;
    axios
      .get(URL)
      .then((res) => {
        this.heritageList = res.data;
      })
      .catch((err) => console.error(err));
  },
  computed: {
    ...mapGetters(["config"]),
  },
  methods: {
    ...mapActions(["setHeritage"]),
  },
  data() {
    return {
      userDataId: "",
      heritageList: [],
      settings: {
        dots: true,
        focusOnSelect: true,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 3,
        touchThreshold: 5,
      },
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/heritage/heritageCarousel.scss";
</style>
