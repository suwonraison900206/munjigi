<template>
  <div>
    <h2>찜한 문화재 목록</h2>
    <div v-if="isEmpty">
      아직 등록된 문화재가 없습니다.
      <button @click="goHeritage">추천 문화재 보러가기</button>
    </div>
    <div v-else>
      <v-container fluid>
        <v-row dense>
          <v-col v-for="(dib, i) in dibData" :key="i" cols="12" sm="2">
            <v-card
              class="mx-auto cursor"
              max-width="300"
              outlined
              @click="goDib(dib.id)"
            >
              <v-list-item three-line>
                <v-list-item-content>
                  <h5>{{ dib.h_name }}</h5>
                  <v-list-item-title>
                    <h4>{{ dib.k_name }}</h4>
                  </v-list-item-title>
                </v-list-item-content>
                <v-list-item-avatar tile size="80" color="grey">
                  <v-img :src="dib.imageurl"></v-img>
                </v-list-item-avatar>
              </v-list-item>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";

export default {
  name: "MypageDib",
  created() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.mypage + sessionStorage.nickname + "/")
      .then((res) => {
        this.dibData = res.data.user.dibs_heritages;
        if (this.dibData.length) {
          this.isEmpty = false;
        } else {
          this.isEmpty = true;
        }
      })
      .catch((err) => console.error(err));
  },
  methods: {
    goHeritage() {
      this.$router.push({ name: "Heritage" });
    },
    goDib(dib) {
      this.$router.push({ name: "HeritageCardDetail", params: { id: dib } });
    },
  },
  data() {
    return {
      isEmpty: true,
      dibData: [],
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/mypage/mypageDib.scss";
</style>

