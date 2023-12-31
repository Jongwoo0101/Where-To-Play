<template>
  <div id="map" ref="map">
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
    height: 30vh;
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
      loadMap(createElement) { // 맵을 그리는 함수 + 백엔드 서버에서 저장된 위치 정보들을 불러옴
        var centerPos = new kakao.maps.LatLng(37.49533610932167, 127.05665437437267)
        const container = document.getElementById('map');
        const options = {
          center: centerPos,
          level: 6,
          mapTypeId: kakao.maps.MapTypeId.HYBRID
        };
        this.map = new kakao.maps.Map(container, options)

        if (navigator.geolocation && (localStorage.getItem('currentPos') == null)) { // 현재 위치로 이동
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
        var isMobileDevice = 'ontouchstart' in this.$refs.map
        console.log(isMobileDevice)
        axios.get(process.env.VUE_APP_BACKEND_ADDRESS+"/place/get/") // 장소 정보를 불러와 맵에 담기
        .then((response) => {
          for (let i = 0; i < response.data.length; i++) {
            let position = new kakao.maps.LatLng(response.data[i].lat, response.data[i].lng);
            if (isMobileDevice) {
              let openContent =
                response.data[i].name + ' / ' + response.data[i].address;
              let toggleContent = document.createElement('div')
              toggleContent.textContent = ''
              toggleContent.style.cssText = 'padding: 7px; background-color: #00FF00; border-radius: 7px; opacity: 50%;'
              let customOverlay = new kakao.maps.CustomOverlay({
                map: this.map,
                content: toggleContent,
                position: position
              })
              toggleContent.addEventListener('touchstart', () => { // 모바일 터치 정보 토글 이벤트
                customOverlay.setMap(null)
                if (toggleContent.textContent === '') {
                  toggleContent.style.cssText = 'padding: 1px; background-color: white; border-radius: 5px; opacity: 70%;'
                  toggleContent.textContent = openContent
                  setTimeout(() => {
                    this.$emit('placeInfo', response.data[i].id)
                  }, 1000);
                } else {
                  toggleContent.textContent = ''
                  toggleContent.style.cssText = 'padding: 7px; background-color: #00FF00; border-radius: 7px; opacity: 50%'
                } 
                customOverlay = new kakao.maps.CustomOverlay({
                  map: this.map,
                  content: toggleContent,
                  position: position
                })
                customOverlay.setMap(this.map)
              })
              customOverlay.setMap(this.map)
            } else {
              let marker = new kakao.maps.Marker({
              position: position,
              map: this.map,
              clickable: true
              });
              let content = '<p style="text-align: left; padding: 10px; border-radius: 5px;">'+ response.data[i].name +' <br> '+ response.data[i].address + '</p>';
              let infoWindow = new kakao.maps.InfoWindow({
                content: content,
              });
              kakao.maps.event.addListener(marker, 'mouseover', this.makeOverListener(toRaw(this.map), marker, infoWindow, response.data[i].id))
              kakao.maps.event.addListener(marker, 'mouseout', this.makeOutListener(infoWindow))
            }
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
      makeOverListener(map, marker, infowindow, id) {
        var here = this
        return function() {
          here.$emit('placeInfo', id)
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