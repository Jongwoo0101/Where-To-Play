<template>
    <div class="container">
        <Map />
        <div class="place-cards">
            <p>운동장 목록</p>
            <div class="card-zone">
                <PlaceCard
                :key="key"
                v-for="data in placeInfo"
                :placeId="data.id"
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
        margin: auto;
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
        position: relative;
        z-index: 2;
        overflow: scroll;
    }
    @media screen and (min-width: 960px) {
        .container {
            grid-template-columns: 3fr 1fr;
            width: 85vw;
            height: 80vh;
            border-radius: 10px;
            box-shadow: 0px 8px 15px rgb(119, 119, 119);
            overflow: hidden;
        }
        .card-zone {
            height: 75vh;
        }
    }
    @media screen and (max-width: 960px) {
        .container { grid-template-rows: 50vh 50vh; }
        .place-cards {
            height: 100vw;
        }
        .card-zone {
            height: 100vw;
        }
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
                placeInfo: null,
                key: 0
            }
        },
        mounted() {
            axios.get(process.env.VUE_APP_BACKEND_ADDRESS+'/place/get/')
            .then((res) => {
                this.placeInfo = res.data
            })
            .catch((e) => {
                alert('장소 세부 정보를 불러오는 데 실패했습니다!')
            })
        },
        methods: {
            updateView() {
                this.key += 1;
            }
        }
    }
</script>