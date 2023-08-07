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
        padding: 1vw;
    }
    .place-cards {
        margin: 0 0 0 1vw;
        display: block;
    }
    @media screen and (min-width: 960px) {
        .container {
            grid-template-columns: 3fr 1fr;
        }

    }
    @media screen and (max-width: 960px) {
        .container { grid-template-rows: 1fr 4fr; }
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