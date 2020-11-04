<template>
  <div class="heritage">
    <div class="searchBar">
      <h2 @click="$router.push({ name: 'HeritageSearchBar' })">
        <v-icon>mdi-magnify</v-icon>문화재 검색하기
      </h2>
    </div>
    <HeritageCarousel />
    <HeritageCards />
  </div>
</template>

<script>
import HeritageCarousel from "@/components/heritage/HeritageCarousel";
import HeritageCards from "@/components/heritage/HeritageCards";

export default {
  name: "Heritage",
  components: {
    HeritageCarousel,
    HeritageCards,
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/views/heritage.scss";
</style>