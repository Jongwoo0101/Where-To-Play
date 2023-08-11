<template>
<div @click="click()" class="card" :id="placeId">
  <div class="card-image">
    <figure class="image is-4by3">
      <img :src="'http://localhost:8000/'+placeImage" alt="Placeholder image">
    </figure>
  </div>
  <div class="card-content">
    <div class="content">
      <p class="title is-4">{{ placeName }}</p>
      <p>{{ placeLocation }}</p>
      <p>{{ placeDescription }}</p>
      <p class="place-details" v-if="placeDetail">
        연락처: {{ response.contact }}<br>
        홈페이지: <a :href="response.homepage" target="_blank">Link</a><br>
        운영 시간: {{ response.time }}
      </p>
    </div>
  </div>
</div>
</template>

<style src="@/assets/bulma.min.css" scoped>
</style>

<script>
  import axios from 'axios';
    export default {
      name: 'PlaceCard',
      props: {
        placeId: '',
        placeImage: null,
        placeName: "장소 이름",
        placeLocation: "장소 위치",
        placeDescription: "장소 설명",
      },
      data() {
        return {
          placeDetail: false,
          response: null,
        }
      },
      methods: {
        click() {
          if (this.placeDetail === false) {
            axios
            .get('http://localhost:8000/place/get/'+this.placeId+'/')
            .then(res => {
              this.placeDetail = !this.placeDetail
              console.log(res.data)
              this.response = res.data
              if (this.response.homepage.search("https://") != 0 && this.response.homepage.search("http://") != 0)
                this.response.homepage = "//" + this.response.homepage
            })
          } else {
            this.placeDetail = !this.placeDetail
          }
        }
      }
    }
</script>