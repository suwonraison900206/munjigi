<template>
  <div class="signup">
    <div class="box">
      <h1>회원가입</h1>
      <!-- 닉네임 -->
      <div>
        <h2>닉네임</h2>
        <!-- 닉네임 input tag -->
        <input
          type="text"
          v-model="signupData.nickname"
          placeholder="닉네임을 입력해주세요"
          @focusout="verifyNickname"
        />
        <h4 v-show="isNicknameVerified" :class="{ 'green--text': isNicknameVerified }">사용가능한 닉네임 입니다!</h4>
        <h4 v-show="!isNicknameVerified" :class="{ 'red--text': !isNicknameVerified }">사용할 수 없는 닉네임입니다</h4>
      </div>

      <!-- 이메일 -->
      <div>
        <h2>이메일</h2>
        <!-- 이메일 input tag -->
        <input
          type="text"
          placeholder="이메일을 입력해주세요"
          v-model="signupData.email"
          @focusout="verifyEmail"
        />
        <h4 v-show="!isEmailValidate" :class="{ 'red--text': !isEmailValidate }">올바른 이메일 형식을 입력해주세요</h4>
        <h4 v-show="isEmailVerified" :class="{ 'green--text': isEmailVerified }">사용가능한 이메일 입니다!</h4>
        <h4 v-show="!isEmailVerified" :class="{ 'red--text': !isEmailVerified }">사용할 수 없는 이메일 입니다</h4>
      </div>

      <!-- 비밀번호 -->
      <div>
        <h2>비밀번호</h2>
        <input type="password" placeholder="비밀번호를 입력해주세요" v-model="signupData.password" />
      </div>

      <!-- 비밀번호 확인 -->
      <div>
        <h2>비밀번호 확인하기</h2>
        <input type="password" placeholder="비밀번호를 한번 더 입력해주세요" v-model="passwordConfirm" />
        <h4 v-show="isPasswordValidate" :class="{ 'green--text': isPasswordValidate }">비밀번호가 일치합니다</h4>
        <h4 v-show="!isPasswordValidate" :class="{ 'red--text': !isPasswordValidate }">비밀번호가 일치하지 않습니다</h4>
      </div>

      <!-- 비밀번호 일치 여부 확인 -> active 넣어야 함 -->
      <div>
        <v-btn
          :disabled="!(isEmailVerified && isNicknameVerified && isEmailValidate && isPasswordValidate)"
          @click="signup(signupData)"
        >
          회원 가입 하기
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import "@/assets/css/views/signup.scss";
import SERVER from "@/api/drf";
import axios from "axios";
import { mapActions } from "vuex";

export default {
  name: "Signup",
  computed: {
    isEmailValidate() {
      const email = this.signupData.email;
      const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return pattern.test(email);
    },
    isPasswordValidate() {
      return !!this.signupData.password && this.signupData.password === this.passwordConfirm
    }
  },
  methods: {
    ...mapActions(["signup"]),
    verifyNickname() {
      const nickname = this.signupData.nickname;
      if (!!nickname === true) {
        axios
          .get(SERVER.URL + SERVER.ROUTES.validity + nickname + "/")
          .then((res) => this.isNicknameVerified = res.data )
      }
    },
    verifyEmail() {
      const email = this.signupData.email;
      if (this.isEmailValidate) {
        axios
          .get(SERVER.URL + SERVER.ROUTES.validity + email + "/")
          .then((res) => this.isEmailVerified = res.data )
      }
    },
  },
  data() {
    return {
      passwordConfirm: null,
      signupData: {
        nickname: "",
        email: "",
        password: "",
      },
      isNicknameVerified: false,
      isEmailVerified: false,
    };
  },
};
</script>

<style>
</style>