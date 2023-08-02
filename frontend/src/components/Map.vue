<template>
    <div id="map">
    </div>
</template>

<style scoped>
  #map {
    margin: auto;
    width: 80vw;
    height: 80vh;
  }
</style>

<script>
    export default {  
      name: 'Map',
      mounted() {
      if (window.kakao && window.kakao.maps) {
        this.loadMap()
      } else {
        this.loadAPI()
      }
    },
    data() {
      return {
        map: null,
        location: null,
      };
    },
    methods: {
      loadAPI() { // API를 불러와 저장하는 함수
        const script = document.createElement("script");
        script.src =
        "https://dapi.kakao.com/v2/maps/sdk.js?appkey=" + process.env.VUE_APP_KAKAO_JS_APPKEY + "&autoload=false";
        script.onload = () => window.kakao.maps.load(this.loadMap);
        document.head.appendChild(script);
      },
      loadMap() { // 맵을 그리는 함수 + 백엔드 서버에서 저장된 위치 정보들을 불러옴
        const container = document.getElementById('map');
        const options = {
          center: new window.kakao.maps.LatLng(37.49533610932167, 127.05665437437267),
          level: 5
        };
        this.map = new window.kakao.maps.Map(container, options)
      },
    }
    }
</script>