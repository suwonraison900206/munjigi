# FRONT END
contributers: 신유빈, 김진혁

## Vue

### vue convention

```jsx
// path는 현재위치표시(./)를 제외하고는 절대경로(@ -> src폴더)를 사용해 주세요
import Home from '@/views/Home.vue'

// 경로는 가급적 이름을 사용해 주세요
<router-link :to="{ name: 'Home' }">Home</router-link>

// 모든 컴포넌트의 script 순서는 다음과 같이 해주세요
export default {
  name, components: {}, props: {}, 
	beforeCreate() {}, created() {},
  beforeMount() {}, mounted() {},
  beforeUpdate() {}, update() {},
  beforeDestroy() {}, destroyed() {},
  computed: {}, watch: {}, methods: {},
  data() { return {} }
}

// 함수는 가급적 (){} 를 사용합니다
changeValue() {} // Yes!
changeValue: function() {} // No!

// mutations.js 에 사용되는 함수들은 SNAKE_CASE를 이용해주세요
ADD_COUNT(state) { state.count++ }

```

## main.js

- 사용할 라이브러리들이 추가되어 있음
- 추가는 상관 없으나 수정을 해야 할 경우 동료에게 말하고 여기에 수정내용을 적어주세요

## routes.js

- vue에서 사용할 path들이 담겨 있음
- 맨 위에 사용할 컴포넌트를 추가하고 밑에 설정을 하면 됨

## vuex 폴더

- store.js, getters.js, actions.js, mutations.js 네 개의 파일이 존재
- 실질적으로 저장되는 store.js에 변수들이 담기며 main.js로의 전송을 담당


## 사용한 라이브러리

- axios
- core-js
- es6-promise
- vue
- vue-router
- vue-slick-carousel
- vuetify
- vuex
