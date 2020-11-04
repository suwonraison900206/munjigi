<template>
  <div class="mypage-profile">
    <h1>{{ userData.user.nickname }}님의 마이페이지</h1>
    <v-row justify="space-between">
      <v-col>
        <img :src="userImage" />
        <div>
          <input type="file" @change="previewImage" accept="image/*" />
        </div>
        <div>
          <p>
            미리보기 준비 중 : {{ uploadValue.toFixed() + "%" }}
            <progress id="progress" :value="uploadValue" max="100"></progress>
          </p>
          <v-btn @click="submitFile">업로드하기</v-btn>
        </div>
      </v-col>
      <v-col>
        <h3>이름 : {{ userData.name }}</h3>
        <h3>나의 신분 "{{ userGrade.rank }}"</h3>
        <img :src="userGrade.image" />
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
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import firebase from "firebase";

export default {
  name: "MypageProfile",
  mounted() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.mypage + sessionStorage.nickname + "/")
      .then((res) => {
        this.userData = res.data;
        this.userImage = res.data.profile_image;
        let userGradeNum = res.data.user.user_review.length;
        if (userGradeNum >= 50) {
          this.userGrade = this.gradeList[0];
        } else if (userGradeNum >= 40) {
          this.userGrade = this.gradeList[1];
        } else if (userGradeNum >= 30) {
          this.userGrade = this.gradeList[2];
        } else if (userGradeNum >= 20) {
          this.userGrade = this.gradeList[3];
        } else if (userGradeNum >= 10) {
          this.userGrade = this.gradeList[4];
        } else if (userGradeNum >= 5) {
          this.userGrade = this.gradeList[5];
        } else {
          this.userGrade = this.gradeList[6];
        }
      })
      .catch((err) => console.error(err));
  },
  methods: {
    previewImage(event) {
      this.uploadValue = 0;
      this.picture = null;
      this.imageData = event.target.files[0];
      this.onUpload();
    },
    onUpload() {
      this.picture = null;
      const storageRef = firebase
        .storage()
        .ref(`${this.imageData.name}`)
        .put(this.imageData);
      storageRef.on(
        `state_changed`,
        (snapshot) => {
          this.uploadValue =
            (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        },
        (error) => {
          console.error(error.message);
        },
        () => {
          this.uploadValue = 100;
          storageRef.snapshot.ref.getDownloadURL().then((url) => {
            this.picture = url;
            this.userImage = url;
          });
        }
      );
    },
    submitFile() {
      const data = {
        name: this.userData.name,
        lastname: this.userData.lastname,
        profile_image: this.userImage,
        birth: this.userData.birth,
      };
      axios
        .put(
          SERVER.URL + SERVER.ROUTES.mypage + sessionStorage.nickname + "/",
          data,
          null
        )
        .then(() => {
          axios
            .get(
              SERVER.URL + SERVER.ROUTES.mypage + sessionStorage.nickname + "/"
            )
            .then((res) => {
              this.userData = res.data;
              this.uploadValue = 0;
              this.userImage = res.data.profile_image;
              alert("프로필이미지가 변경되었습니다.");
            })
            .catch((err) => console.error(err));
        })
        .catch((err) => console.error(err));
    },
  },
  data() {
    return {
      gradeInfo: false,
      userData: "",
      userImage: "",
      imageData: null,
      picture: null,
      uploadValue: 0,
      file: "",
      selectedFile: null,
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
      userGrade: 0,
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/mypage/mypageProfile.scss";
</style>
