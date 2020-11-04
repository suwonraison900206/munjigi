<template>
  <div class="maps">
    <MapsKakao />
  </div>
</template>

<script>
import MapsKakao from "@/components/maps/MapsKakao";

export default {
  name: "Maps",
  components: {
    MapsKakao,
  },
  data() {
    return {};
  },
};
</script>

<style lang="scss">
@import "@/assets/css/views/maps.scss";
</style>