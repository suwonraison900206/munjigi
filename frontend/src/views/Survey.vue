<template>
  <div class="survey">
    <div class="survey-box">
      <h1>설문 조사</h1>
      <h4>
        여러분에게 꼭 맞는 문화재를 추천해드리기 위해 필요한 설문조사입니다!
      </h4>
      <h4>시간을 내서 끝까지 진행해주시면 감사하겠습니다!</h4>

      <v-container>
        <!-- 시대 -->
        <v-row>
          <v-col cols="12" sm="4">
            <h3>시대별 선호도 조사</h3>
          </v-col>

          <v-col cols="12" sm="8">
            <v-select
              v-model="e5"
              :items="era"
              label="선택"
              multiple
              chips
              hint="당신이 좋아하는 시대는 무엇인가요?"
              persistent-hint
            ></v-select>
          </v-col>
        </v-row>

        <!-- 인물 -->
        <v-row>
          <v-col cols="12" sm="4">
            <h3>인물별 선호도 조사</h3>
          </v-col>

          <v-col cols="12" sm="8">
            <v-select
              v-model="e6"
              :items="people"
              label="선택"
              multiple
              chips
              hint="알고 싶은 특별한 인물이 있나요?"
              persistent-hint
            ></v-select>
          </v-col>
        </v-row>

        <!-- 문화재 종류 -->
        <v-row>
          <v-col cols="12" sm="4">
            <h3>문화재 종류 선호도 조사</h3>
          </v-col>

          <v-col cols="12" sm="8">
            <v-select
              v-model="e7"
              :items="heritages"
              label="선택"
              multiple
              chips
              hint="좋아하는 문화재에는 어떤 것이 있나요?"
              persistent-hint
            ></v-select>
          </v-col>
        </v-row>
      </v-container>

      <br />
      <!-- 제출버튼 -->
      <div>
        <v-btn class="button" :disabled="!arr.length" @click="submitSurvey"
          >제 출</v-btn
        >
      </div>
    </div>
  </div>
</template>

<script>
import "@/assets/css/views/survey.scss";
import axios from "axios";
import SERVER from "@/api/drf";
import { mapGetters } from "vuex";

export default {
  name: "Survey",
  computed: {
    ...mapGetters(["config"]),
    arr() {
      return [...this.e5, ...this.e6, ...this.e7];
    },
  },
  methods: {
    submitSurvey() {
      const URL = SERVER.URL + SERVER.ROUTES.survey;
      axios
        .post(URL, this.arr, this.config)
        .then(() => {
          alert(
            "설문조사에 응해 주셔서 감사합니다! 결과가 이제 추천시스템에 반영됩니다."
          );
          this.$router.push({ name: "Home" });
        })
        .catch();
    },
  },
  data() {
    return {
      dataObject: {
        청동기시대: 1015,
        철기시대: 9194,
      },
      e5: [],
      e6: [],
      e7: [],
      era: [
        "청동기시대",
        "철기시대",
        "삼국시대",
        "통일신라",
        "남북국시대",
        "고려시대",
        "조선시대",
      ],
      people: [
        "영조",
        "장영실",
        "태종",
        "정도전",
        "이순신",
        "선조",
        "이황",
        "이이",
        "김홍도",
        "신윤복",
        "이성계",
      ],
      heritages: [
        "불상",
        "백자",
        "청자",
        "토기",
        "석탑",
        "목탑",
        "절",
        "고궁",
        "절터",
        "탱화",
        "벽화",
        "가구",
      ],
    };
  },
};
</script>

