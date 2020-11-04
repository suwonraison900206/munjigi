<template>
  <div class="otherpage">
    <div class="other-profile">
      <h1>{{ OtherData.user.nickname }}님의 마이페이지</h1>
      <v-row justify="space-between">
        <v-col>
          <img class="otherpage-img" :src="OtherData.profile_image" />
        </v-col>
        <v-col>
          <h3>이름 : {{ OtherData.name }}</h3>

          <h3>나의 신분 "{{ otherGrade.rank }}"</h3>
          <img :src="otherGrade.image" />
          <div>
            <v-dialog v-model="gradeInfo" width="600px">
              <template v-slot:activator="{ on, attrs }">
                <v-btn class="ma-2" tile outlined v-bind="attrs" v-on="on"
                  >신분제알아보기</v-btn
                >
              </template>
              <v-card>
                <v-card-title>
                  <h1>문지기의 신분제</h1>
                  <h4>작성한 리뷰의 개수로 신분이 결정됩니다.</h4>
                </v-card-title>

                <div v-for="(grade, idx) in gradeList" :key="idx">
                  <img class="grade-image" :src="grade.image" />
                  <span class="grade-text">
                    {{ grade.rank }}
                  </span>
                  <span class="grade-number"
                    >리뷰 {{ grade.number }}개 이상일 경우</span
                  >
                </div>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn text @click="gradeInfo = false"><h4>닫기</h4></v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </div>
        </v-col>
      </v-row>
    </div>
    <div>
      <h2>찜한 문화재 목록</h2>
      <div v-if="isHEmpty">
        아직 등록된 문화재가 없습니다.
        <button @click="goHeritage">추천 문화재 보러가기</button>
      </div>
      <div v-else>
        <v-container fluid>
          <v-row dense>
            <v-col v-for="(dib, i) in dibData" :key="i" cols="12" sm="2">
              <v-card
                class="mx-auto cursor"
                max-width="300"
                outlined
                @click="goDib(dib.id)"
              >
                <v-list-item three-line>
                  <v-list-item-content>
                    <h5>{{ dib.h_name }}</h5>
                    <v-list-item-title>
                      <h4>{{ dib.k_name }}</h4>
                    </v-list-item-title>
                  </v-list-item-content>
                  <v-list-item-avatar tile size="80" color="grey">
                    <v-img :src="dib.imageurl"></v-img>
                  </v-list-item-avatar>
                </v-list-item>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
    <div>
      <h2>문화재 리뷰 작성 목록</h2>
      <div v-if="isEmpty">
        아직 등록된 리뷰가 없습니다.
        <div>
          <v-btn @click="$router.push({ name: 'Community' })">
            게시판으로 가기
          </v-btn>
        </div>
      </div>

      <div v-else>
        <ul v-for="(review, i) in reviewData" :key="i">
          <div @click="SELECT_REVIEW(review)">
            <h3 class="review-pick">{{ review.title }}</h3>
            {{ review.created_at }}
          </div>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import { mapMutations } from "vuex";

export default {
  name: "Otherpage",
  mounted() {
    axios
      .get(
        SERVER.URL + SERVER.ROUTES.mypage + this.$route.params.nickname + "/"
      )
      .then((res) => {
        this.reviewData = res.data.user.user_review;
        if (this.reviewData.length) {
          this.isEmpty = false;
        } else {
          this.isEmpty = true;
        }
        this.dibData = res.data.user.dibs_heritages;
        if (this.dibData.length) {
          this.isHEmpty = false;
        } else {
          this.isHEmpty = true;
        }
        this.OtherData = res.data;
        let otherGradeNum = res.data.user.user_review.length;
        if (otherGradeNum >= 50) {
          this.otherGrade = this.gradeList[0];
        } else if (otherGradeNum >= 40) {
          this.otherGrade = this.gradeList[1];
        } else if (otherGradeNum >= 30) {
          this.otherGrade = this.gradeList[2];
        } else if (otherGradeNum >= 20) {
          this.otherGrade = this.gradeList[3];
        } else if (otherGradeNum >= 10) {
          this.otherGrade = this.gradeList[4];
        } else if (otherGradeNum >= 5) {
          this.otherGrade = this.gradeList[5];
        } else {
          this.otherGrade = this.gradeList[6];
        }
      })
      .catch((err) => console.error(err));
  },
  methods: {
    ...mapMutations(["SELECT_REVIEW"]),
    goHeritage() {
      this.$router.push({ name: "Heritage" });
    },
    goDib(dib) {
      this.$router.push({ name: "HeritageCardDetail", params: { id: dib } });
    },
  },
  data() {
    return {
      gradeInfo: false,
      otherNickname: "",
      OtherData: "",
      reviewData: "",
      isEmpty: true,
      isHEmpty: true,
      dibData: [],
      gradeList: [
        {
          image:
            "https://user-images.githubusercontent.com/60081201/95014433-bf99af00-0681-11eb-8b44-e47fecfbd981.jpg",
          rank: "왕",
          number: "50",
        },
        {
          image:
            "https://user-images.githubusercontent.com/60081201/95014434-c0324580-0681-11eb-8079-71b1c9228d0a.jpg",
          rank: "중전",
          number: "40",
        },
        {
          image:
            "https://user-images.githubusercontent.com/60081201/95014436-c0cadc00-0681-11eb-97e7-1c6e5cda9ea6.jpg",
          rank: "관료",
          number: "30",
        },
        {
          image:
            "https://user-images.githubusercontent.com/60081201/95014437-c0cadc00-0681-11eb-95c0-c2d78b5b5868.jpg",
          rank: "사또",
          number: "20",
        },
        {
          image:
            "https://user-images.githubusercontent.com/60081201/95014431-bf011880-0681-11eb-94ef-2fd7491fedc3.jpg",
          rank: "아씨",
          number: "10",
        },
        {
          image:
            "https://user-images.githubusercontent.com/60081201/95014429-bdcfeb80-0681-11eb-9f88-aaf228187bca.png",
          rank: "상민",
          number: "5",
        },
        {
          image:
            "https://user-images.githubusercontent.com/60081201/95014435-c0324580-0681-11eb-9387-9bde492766e9.jpg",
          rank: "천민",
          number: "0",
        },
      ],
      otherGrade: 0,
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/views/otherpage.scss";
</style>