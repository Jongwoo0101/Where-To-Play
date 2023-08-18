<template>
  <div id="map">
    <button class="refresh-btn" @click="refreshCurrentPos()">현위치 불러오기</button>
  </div>
</template>

<style scoped>
#map {
  position: relative;
  width: 100%;
  z-index: 1;
  background-color: black;
}
.refresh-btn {
  position: relative;
  right: 0;
  margin: 5px 0 0 0;
  width: 100px;
  height: 45px;
  z-index: 2;
  border: 0;
  background-color: #485fc7;
  color: white;
  border-radius: 10px;
  box-shadow: 0px 8px 15px rgba(255, 255, 255, 0.3);
}
@media screen and (max-width: 960px) {
  #map {
    height: 50vh;
  }
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
        "https://dapi.kakao.com/v2/maps/sdk.js?appkey=" + process.env.VUE_APP_KAKAO_JS_APPKEY + "&libraries=services&autoload=false";
        script.onload = () => window.kakao.maps.load(this.loadMap);
        document.head.appendChild(script);
      },
      loadMap() { // 맵을 그리는 함수 + 백엔드 서버에서 저장된 위치 정보들을 불러옴
        var centerPos = new kakao.maps.LatLng(37.49533610932167, 127.05665437437267)
        const container = document.getElementById('map');
        const options = {
          center: centerPos,
          level: 6,
          mapTypeId: kakao.maps.MapTypeId.HYBRID
        };
        this.map = new kakao.maps.Map(container, options)

        if (navigator.geolocation && (localStorage.getItem('currentPos') == null)) {
          navigator.geolocation.getCurrentPosition((pos) => {
            localStorage.setItem('currentPos', [pos.coords.latitude, pos.coords.longitude])
            let currentPos = localStorage.getItem('currentPos').split(',')
            currentPos = new kakao.maps.LatLng(currentPos[0], currentPos[1])
            this.map.panTo(currentPos)
          })
        } else if (localStorage.getItem('currentPos') != null) {
          let currentPos = localStorage.getItem('currentPos').split(',')
          currentPos = new kakao.maps.LatLng(currentPos[0], currentPos[1])
          this.map.panTo(currentPos)
        } else {
          alert("[ERROR] 현재 위치를 불러올 수 없습니다.")
        }
        
        this.geocoder = new kakao.maps.services.Geocoder();
        
        axios.get(process.env.VUE_APP_BACKEND_ADDRESS+"/place/get/")
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
        })
      },
      clickEvent(mouseEvent) { // 마우스 클릭 시 좌표를 가져오기 위한 함수
        let latlng = mouseEvent.latLng;
        let message = latlng.getLat() + ', ' + latlng.getLng()
        this.location = message;
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
      refreshCurrentPos() {
        if (navigator.geolocation) {
          alert("위치를 불러오는데 시간이 약 10초 이상 소요될 수 있습니다.")
          navigator.geolocation.getCurrentPosition((pos) => {
            localStorage.setItem('currentPos', [pos.coords.latitude, pos.coords.longitude])
            let currentPos = localStorage.getItem('currentPos').split(',')
            currentPos = new kakao.maps.LatLng(currentPos[0], currentPos[1])
            toRaw(this.map.panTo(currentPos))
          })
        } else {
          alert("[ERROR] 현재 위치를 불러올 수 없습니다.")
        }
      }
    }
  }
</script>