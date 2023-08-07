<template>
    <div class="container">
        <Map @place="getInfo"/>
        <div class="placeform">
            <input @change="uploadImage" type="file" accept="image/*">
            <input v-model="placeName" type="text" placeholder="장소명(필수)">
            <input v-model="placeAddress" type="text" placeholder="위치">
            <input v-model="placeContact" type="text" placeholder="연락처">
            <input v-model="placeHomepage" type="text" placeholder="홈페이지">
            <input v-model="placeTime" type="text" placeholder="운영시간">
            <textarea v-model="placeDescription" placeholder="여기는 어떤 장소인지 설명해주세요!"></textarea>
            <legend><input type="checkbox">[선택] 개인정보 수집 및 이용 동의</legend>
            <button @click="submit()">장소 등록!</button>
        </div>
    </div>
</template>

<style scoped>
    .container {
        display:grid;
        grid-template-columns: 4fr 1fr;
    }
    .placeform {
        display: grid;
        grid-template-rows: repeat(15, 1fr);
        margin: 1vw;
    }
    .placeform > input[type=text],input[type=file],texarea {
        margin-top: 1vh;
        display: block;
    }
</style>

<script>
    import Map from '@/components/Map.vue';
    import axios from 'axios'
    export default {
        name: "AddPlace",
        components: {
            Map
        },
        data() {
            return {
                placeAddress: null,
                placeLocation: null,
                image: '',
                placeName: '',
                placeContact: '',
                placeHomepage: '',
                placeTime: '',
                placeDescription: ''
            }
        },
        methods: {
            getInfo(location) {
                this.placeLocation = location[0];
                this.placeAddress = location[1];
                console.log(location)
            },
            uploadImage(imageFile) {
                this.image = imageFile
            },
            submit() {
                if ((this.placeAddress != null)&&
                     (this.placeContact != null)&&
                     (this.placeDescription != null)&&
                     (this.placeHomepage != null)&&
                     (this.placeLocation != null)&&
                     (this.placeName != null)&&
                     (this.placeTime != null)&&
                     (this.image != '')
                    )
                {
                console.log (this.image)
                let date = new Date().toJSON();
                const position = this.placeLocation.split(', ');
                const formData = new FormData()
                formData.append('image', this.image.originalTarget.files[0])
                formData.append('name', this.placeName)
                formData.append('lat', position[0])
                formData.append('lng', position[1])
                formData.append('address', this.placeAddress)
                formData.append('contact', this.placeContact)
                formData.append('homepage', this.placeHomepage)
                formData.append('time', this.placeTime)
                formData.append('description', this.placeDescription)
                formData.append('created_at', date)
                formData.append('updated_at', date)
                console.log(formData)
                axios.post("http://localhost:8000/place/addplace/", 
                    formData
                    ,{ headers: { 'Content-Type': 'multipart/form-data', Authorization: 'Token '+sessionStorage.getItem('userToken')}
                })
                .then(res => {
                    console.log(res)
                })
                .catch(e => {
                    console.log(e)
                })
            } else {
                alert("모든 정보를 다 입력해주세요!")
            }
        }
        }
    }
</script>