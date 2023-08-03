<template>
    <div class="container">
        <Map />
        <div class="placeform">
            <input type="file" accept="image/*">
            <input type="text" placeholder="장소명(필수)">
            <input type="text" placeholder="위치">
            <input type="text" placeholder="연락처">
            <input type="text" placeholder="홈페이지">
            <input type="text" placeholder="운영시간">
            <textarea placeholder="여기는 어떤 장소인지 설명해주세요!"></textarea>
            <legend><input type="checkbox">[선택] 개인정보 수집 및 이용 동의</legend>
            <button>장소 등록!</button>
        </div>
    </div>
</template>

<style scoped>
    .container {
        display: flex;
    }
    .placeform {
        display: grid;
        grid-template-rows: repeat(15, 1fr);
    }
    .placeform > input[type=text],input[type=file],texarea {
        margin-top: 1vh;
        display: block;
    }
</style>

<script>
    import Map from '@/components/Map.vue';

    export default {
        name: "AddPlace",
        components: {
            Map
        }
    }
</script>