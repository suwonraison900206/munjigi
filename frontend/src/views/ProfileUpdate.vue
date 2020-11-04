<template>
  <div class="profile-update">
    <h1 class="profile-update-header">개인 정보 수정</h1>
    <div class="profile-update-block">
      <h3>이메일</h3>
      <span>이메일 주소는 변경하실 수 없습니다.</span>
      <input type="text" disabled v-model="email" />
    </div>
    <div class="profile-update-block">
      <h3>이름</h3>
      <input type="text" v-model="userData.name" />
    </div>
    <div class="profile-update-block">
      <h3>조상 성씨</h3>
      <input type="text" v-model="userData.lastname" />
    </div>
    <div class="profile-update-block">
      <h3>생년월일</h3>
      <input type="text" v-model="userData.birth" />
    </div>

    <div class="submit-buttons">
      <input type="submit" value="나가기" @click="goPreviousPage" />
      <input type="submit" value="작성완료" @click="changeUserInfo" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SERVER from "@/api/drf";
import "@/assets/css/views/profileUpdate.scss";
import { mapGetters } from "vuex";

export default {
  name: "ProfileUpdate",
  created() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.mypage + sessionStorage.nickname + "/")
      .then((res) => {
        this.userData.name = res.data.name;
        this.userData.lastname = res.data.lastname;
        this.userData.profile_image = res.data.profile_image;
        this.userData.birth = res.data.birth;
      });
  },
  computed: {
    ...mapGetters(["config"]),
  },
  methods: {
    changeUserInfo() {
      const data = {
        name: this.userData.name,
        lastname: this.userData.lastname,
        profile_image: this.userData.profile_image,
        birth: this.userData.birth,
      };
      axios
        .put(
          SERVER.URL + SERVER.ROUTES.mypage + sessionStorage.nickname + "/",
          data,
          null
        )
        .then(() => {
          alert("개인 정보가 수정되었습니다.");
          sessionStorage["birth"] = this.userData.birth;
          sessionStorage["lastname"] = this.userData.lastname;
          sessionStorage["name"] = this.userData.name;
          this.$router.push({ name: "Mypage" });
        })
        .catch((err) => console.error(err));
    },
    goPreviousPage() {
      this.$router.go(-1);
    },
  },
  data() {
    return {
      userData: {
        name: null,
        id: sessionStorage.getItem("id"),
        lastname: "",
        profile_image: null,
        birth: null,
      },
      email: sessionStorage.getItem("email"),
      nickname: sessionStorage.getItem("nickname"),
    };
  },
};
</script>

