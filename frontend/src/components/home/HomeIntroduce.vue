<template>
  <div class="homeIntroduce">
    <h1>문지기란?</h1>

    <div class="v-cards-container">
      <div
        v-for="(item, i) in items"
        :key="i"
        class="v-card"
        @click="$router.push({ name: item.location })"
      >
        <v-img :src="item.img" gradient="rgba(0,0,0,.5), rgba(0,0,0,.5)">
          <h1 class="card-title">{{ item.title }}</h1>
          <h2 class="card-title">{{ item.text }}</h2>
        </v-img>
      </div>
    </div>
  </div>
</template>

<script>
import "@/assets/css/components/home/homeIntroduce.scss";

export default {
  name: "HomeIntroduce",
  data: () => ({
    items: [
      {
        title: "문화재 추천",
        text: "사용자만을 위한 추천 서비스",
        img:
          "https://user-images.githubusercontent.com/60081201/93179267-66b8b400-f770-11ea-9227-8edb275c138d.png",
        location: "Heritage",
      },
      {
        title: "게시판",
        text: "문화재 방문 리뷰 공유",
        img:
          "https://user-images.githubusercontent.com/60081201/93179265-65878700-f770-11ea-923c-f7fed06a90a0.png",
        location: "Community",
      },
      {
        title: "지도",
        text: "문화재 주변 정보 제공",
        img:
          "https://user-images.githubusercontent.com/60081201/93179269-67514a80-f770-11ea-8975-1f6f3a2b0a18.png",
        location: "Maps",
      },
    ],
  }),
};
</script>

<style>
</style>

