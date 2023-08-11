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
      methods: {
        click() {
          axios
          .get('http://localhost:8000/place/get/'+this.placeId+'/')
          .then(res => { console.log(res.data) })
        }
      }  
    }
</script>