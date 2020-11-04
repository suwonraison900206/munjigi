<template>
  <div class="login">
    <div class="box">
      <h1>로그인</h1>
      <h2>이메일</h2>
      <input
        type="text"
        v-model="loginData.email"
        placeholder="이메일을 입력해주세요"
        autofocus
        required="이메일을 입력해 주세요!"
      />
      <h2>비밀번호</h2>
      <input
        type="password"
        v-model="loginData.password"
        @keypress.enter="login(loginData)"
        placeholder="비밀번호를 입력해주세요"
        required="비밀번호를 입력해주세요!"
      />
      <h3><input type="submit" value="로그인" @click="login(loginData)" /></h3>
    </div>

    <h3>
      아직 회원이 아니신가요?
      <a href="#" @click="goSignup"> 회원가입하러 가기</a>
    </h3>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Login",
  methods: {
    ...mapActions(["login"]),
    goSignup() {
      this.$router.push({ name: "Signup" });
    },
  },
  data() {
    return {
      loginData: {
        email: "",
        password: "",
      },
    };
  },
};
</script>

<style lang="scss">
@import "@/assets/css/views/login.scss";
</style>