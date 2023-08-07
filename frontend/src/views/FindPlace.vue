<template>
    <div class="container">
        <Map />
        <div class="place-cards">
            <PlaceCard
            v-for="data in placeInfo"
            :placeImage="data.image"
            :placeName="data.name"
            :placeLocation="data.address"
            :placeDescription="data.description"
            />
        </div>
    </div>
</template>

<style scoped>
    .container {
        display: grid;
        grid-template-columns: 3fr 1fr;
        padding: 1vw;
    }
    .place-cards {
        margin: 0 0 0 1vw;
        display: block;
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
            axios.get('http://localhost:8000/place/getplace/')
            .then((res) => {
                console.log(res.data)
                this.placeInfo = res.data
            })
            .catch((e) => { console.log(e) })
        }
    }
</script>