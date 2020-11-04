<template>
  <div class="home">
    <HomeIntroduce />
    <HomeHeritage v-if="hasRecommend" />
    <HomeCalendar />
  </div>
</template>

<script>
import HomeIntroduce from "@/components/home/HomeIntroduce.vue";
import HomeHeritage from "@/components/home/HomeHeritage.vue";
import HomeCalendar from "@/components/home/HomeCalendar.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Home",
  components: {
    HomeIntroduce,
    HomeHeritage,
    HomeCalendar,
  },
  computed: {
    ...mapGetters(["config"]),
    hasRecommend(){
      return !!sessionStorage.id
    }
  },
  methods: {
    ...mapActions(["logout"]),
  },
  data() {
    return {
      id: sessionStorage.getItem("id")
    }
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/views/home.scss";
</style>