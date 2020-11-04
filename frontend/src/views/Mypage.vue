<template>
  <div class="mypage">
    <MypageProfile />
    <MypageDib />
    <MypageReview />
    <div class="mypage-buttons">
      <v-btn dark color="purple" :to="{ name: 'ProfileUpdate' }">
        정보 수정
      </v-btn>
      <MypageDelete />
    </div>
  </div>
</template>

<script>
import MypageProfile from "@/components/mypage/MypageProfile.vue";
import MypageDib from "@/components/mypage/MypageDib.vue";
import MypageReview from "@/components/mypage/MypageReview.vue";
import MypageDelete from "@/components/mypage/MypageDelete.vue";
import "@/assets/css/views/mypage.scss";

export default {
  name: "Mypage",
  components: {
    MypageProfile,
    MypageDib,
    MypageReview,
    MypageDelete,
  },
};
</script>

