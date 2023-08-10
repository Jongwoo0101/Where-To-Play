<template>
    <div class="container">
        <Map />
        <div class="place-cards">
            <p>운동장 목록</p>
            <div class="card-zone">
                <PlaceCard
                v-for="data in placeInfo"
                :placeImage="data.image"
                :placeName="data.name"
                :placeLocation="data.address"
                :placeDescription="data.description"
                />
            </div>
        </div>
    </div>
</template>

<style scoped>
    .container {
        display: grid;
        padding: 1vw;
    }
    .place-cards {
        margin: 0 0 0 0.5vh;
        display: block;
    }
    .card-zone > div {
        margin: 10px auto 10px auto;
    }
    .card-zone {
        height: 95vh;
        overflow: scroll;
    }
    @media screen and (min-width: 960px) {
        .container {
            grid-template-columns: 3fr 1fr;
        }
    }
    @media screen and (max-width: 960px) {
        .container { grid-template-rows: 1fr 4fr; }
    }
    p {
        font-weight: 700;
        font-size: 18pt;
        margin: 0 0 3vh 0;
    }
</style>

<script>
    import axios from 'axios';
    import Map from "@/components/Map.vue"
    import PlaceCard from "@/components/PlaceCard.vue"
    export default {
        name: "FindPlace",
        components: {
            Map,
            PlaceCard
        },
        data() {
            return {
                placeInfo: null
            }
        },
        mounted() {
            axios.get('http://localhost:8000/place/get/')
            .then((res) => {
                console.log(res.data)
                this.placeInfo = res.data
            })
            .catch((e) => { console.log(e) })
        }
    }
</script>