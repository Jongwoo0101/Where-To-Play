<template>
    <div id="map">
    </div>
</template>

<style scoped>
  #map {
    width: 100%;
    height: 100vh;
  }
</style>

<script>
  import axios from 'axios'
  import { toRaw } from 'vue';
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
          kakao.maps.event.addListener(toRaw(this.map), 'click', this.clickEvent);
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
          markers: [],
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
            level: 5,
            mapTypeId: kakao.maps.MapTypeId.HYBRID
          };
          this.map = new kakao.maps.Map(container, options)
          this.geocoder = new kakao.maps.services.Geocoder();
          
          axios.get("http://localhost:8000/place/get/")
          .then((response) => {
            for (let i = 0; i < response.data.length; i++) {
              let position = new kakao.maps.LatLng(response.data[i].lat, response.data[i].lng);
              let marker = new kakao.maps.Marker({
                position: position,
                map: this.map
              });
              let content = '<p style="text-align: left; padding: 10px;">'+ response.data[i].name +' <br> '+ response.data[i].address + '</p>';
              let infoWindow = new kakao.maps.InfoWindow({
                content: content,
              });

              kakao.maps.event.addListener(marker, 'mouseover', this.makeOverListener(toRaw(this.map), marker, infoWindow))
              kakao.maps.event.addListener(marker, 'mouseout', this.makeOutListener(infoWindow))
            }
          })
          .catch((err) => {
            alert("장소 정보들을 불러오는데 실패했습니다.")
            console.log(err)
          })
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
        },
        makeOverListener(map, marker, infowindow) {
          return function() {
            infowindow.open(map, marker);
          };
        },
        makeOutListener(infowindow) {
          return function () {
            infowindow.close();
          };
        },
      }
    }
</script>