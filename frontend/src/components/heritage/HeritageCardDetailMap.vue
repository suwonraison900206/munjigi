<template>
  <div id="cardMap" style="width: 100%; height: 350px; width: 700px; margin: 0 auto;"></div>
</template>

<script>
export default {
  name: "HeritageCardDetailMap",
  props: {
    latitude: {
      type: Number,
    },
    longitude: {
      type: Number,
    },
  },
  mounted() {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
  },
  methods: {
    initMap() {
      var mapContainer = document.getElementById("cardMap"), // 지도를 표시할 div
        mapOption = {
          center: new kakao.maps.LatLng(this.latitude, this.longitude), // 지도의 중심좌표
          level: 3, // 지도의 확대 레벨
        };

      // 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
      var map = new kakao.maps.Map(mapContainer, mapOption);
      
      // 마커가 표시될 위치입니다
      var markerPosition = new kakao.maps.LatLng(this.latitude, this.longitude);

      // 마커를 생성합니다
      var marker = new kakao.maps.Marker({
        position: markerPosition,
      });

      // 마커가 지도 위에 표시되도록 설정합니다
      marker.setMap(map);
    },
    addScript() {
      const script = document.createElement("script");
      /* global kakao */ script.onload = () => kakao.maps.load(this.initMap);
      const API_KEY = process.env.VUE_APP_KAKAO_MAP_KEY;
      script.src = `http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY}&libraries=services`;
      document.head.appendChild(script);
    },
  },
};
</script>

<style>
</style>