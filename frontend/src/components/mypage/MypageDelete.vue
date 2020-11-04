<template>
  <div>
    <v-dialog v-model="gradeInfo" width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn class="ma-2" v-bind="attrs" color="error" v-on="on"
          >회원탈퇴</v-btn
        >
      </template>
      <v-card>
        <v-card-title>
          <h1>탈퇴하시겠습니까?</h1>
        </v-card-title>
        <h3>
          <span>비밀번호 </span>
          <input
            type="password"
            autofocus
            v-model="checkPassword"
            placeholder="비밀번호를 입력해주세요. "
            @keyup.enter="checkPw"
          />
          <v-btn text color="error" @click="checkPw"><h3>확인</h3></v-btn>
        </h3>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="gradeInfo = false"><h3>닫기</h3> </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import { mapMutations } from "vuex";

export default {
  name: "MypageDelete",

  created() {
    if (sessionStorage.getItem("nickname") !== "undefined") {
      this.userData.nickname = sessionStorage.getItem("nickname");
    }
  },
  methods: {
    ...mapMutations(["SET_TOKEN"]),
    checkPw() {
      axios
        .post(
          SERVER.URL +
            SERVER.ROUTES.mypage +
            this.userData.nickname +
            "/passwordcheck" +
            "/",
          {
            password: this.checkPassword,
          },
          null
        )
        .then((res) => {
          if (res.data) {
            axios
              .delete(
                SERVER.URL +
                  SERVER.ROUTES.mypage +
                  sessionStorage.nickname +
                  "/"
              )
              .then(() => {
                alert("탈퇴가 완료되었습니다.");
                this.gradeInfo = false;
                this.SET_TOKEN(null);
                sessionStorage.removeItem("auth-token");
                sessionStorage.removeItem("birth");
                sessionStorage.removeItem("dateJoined");
                sessionStorage.removeItem("email");
                sessionStorage.removeItem("id");
                sessionStorage.removeItem("name");
                sessionStorage.removeItem("nickname");
                this.$router.push({ name: "Home" });
              })
              .catch((err) => console.error(err));
          } else {
            alert("비밀번호가 틀렸습니다.");
            this.checkPassword = "";
          }
        })
        .catch((err) => console.error(err));
    },
  },
  data() {
    return {
      userData: {
        nickname: sessionStorage.getItem("nickname"),
      },
      gradeInfo: false,
      checkPassword: "",
    };
  },
};
</script>

<style>
</style>