<template>
    <div id="map">
    </div>
</template>

<style scoped>
  #map {
    width: 100%;
  }
</style>

<script>
    export default {  
      name: 'Map',

      updated(){
        if (window.kakao && window.kakao.maps) {
          this.loadMap()
          kakao.maps.event.addListener(this.map, 'click', this.clickEvent);
        } else {
          this.loadAPI()
        }
      },
      mounted() {
        if (window.kakao && window.kakao.maps) {
          this.loadMap()
          kakao.maps.event.addListener(this.map, 'click', this.clickEvent);
        } else {
          this.loadAPI()
        }
      },
      data() {
        return {
          map: null,
          location: null,
          address: null,
          geocoder: null,
          placeInfo: null,
        };
      },
      methods: {
        loadAPI() { // API를 불러와 저장하는 함수
          const script = document.createElement("script");
          script.src =
          "http://dapi.kakao.com/v2/maps/sdk.js?appkey=" + process.env.VUE_APP_KAKAO_JS_APPKEY + "&libraries=services&autoload=false";
          script.onload = () => window.kakao.maps.load(this.loadMap);
          document.head.appendChild(script);
        },
        loadMap() { // 맵을 그리는 함수 + 백엔드 서버에서 저장된 위치 정보들을 불러옴
          const container = document.getElementById('map');
          const options = {
            center: new kakao.maps.LatLng(37.49533610932167, 127.05665437437267),
            level: 5
          };
          this.map = new kakao.maps.Map(container, options)
          this.geocoder = new kakao.maps.services.Geocoder();
        },
        clickEvent(mouseEvent) { // 마우스 클릭 시 좌표를 가져오기 위한 함수
          let latlng = mouseEvent.latLng;
          let message = latlng.getLat() + ', ' + latlng.getLng()
          this.location = message;
          console.log("clicked")
          this.geocoder.coord2Address(latlng.getLng(), latlng.getLat(), (result, status) => {
            if (result[0].road_address != null){
              this.address = result[0].road_address.address_name
            } else if(result[0].address != null) {
              this.address = result[0].address.address_name  
            }
            this.sendData()
          })
        },
        sendData() { // 상위 컴포넌트인 AddPlace에서 위치 활용하기 위한 함수
          if (this.address != null) 
            this.$emit('place', [this.location, this.address])
        }
      }
    }
</script>