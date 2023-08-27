<template>
    <div class="container">
        <Map @placeInfo="focusCard"/>
        <div class="place-cards">
            <p>운동장 목록</p>
            <div class="card-zone">
                <PlaceCard
                v-for="data in placeInfo"
                :ref="data.id"
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
        margin: 0 0.5vh 0 0.5vh;
    }
    .card-zone > div {
        margin: 10px auto 10px auto;
    }
    .card-zone {
        position: relative;
        z-index: 2;
        overflow-y: scroll;
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
        .container { grid-template-rows: 30vh 100vh; }
        .place-cards {
            height: 100vh;
        }
        .card-zone {
            height: 100vh;
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
            focusCard(id) {
                console.log(this.$refs[id][0].$el.scrollIntoView({
                    behavior: 'smooth', block: 'start', inline: 'nearest', top: 0
                }))
            } 
        }
    }
</script>