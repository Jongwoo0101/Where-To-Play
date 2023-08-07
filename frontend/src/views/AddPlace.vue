<template>
    <div class="container">
        <Map @place="getInfo"/>
        <div class="placeform">
            <p>장소 등록</p>
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
    p {
        font-weight: 700;
        font-size: 16pt;
        text-align: center;
    }
    .placeform > input[type=text],input[type=file],textarea {
        display: block;
        margin: 1vh auto auto auto;
    }
    .container {
        display: grid;
    }
    input,textarea {
        border: solid 1.5px #000000;
        border-radius: 1rem;
        background: none;
        padding: 1rem;
        font-size: 1rem;
        color: #000000;
        transition: border 150ms cubic-bezier(0.4, 0, 0.2, 1);
    }
    input:focus, textarea:focus {
        outline: none;
        border: 1.5px solid #1a73e8;
    }
    button {
        border: 0;
        box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
        border-radius: 1rem;
        transition: background-color 0.5s;
        background-color: azure;
        margin: 0;
    }

    button:hover {
        transition: background-color 0.5s;
        background-color: #1a73e8;
    }
    legend {
        margin: auto;
    }
    @media screen and (min-width: 960px) {
        .container {
            grid-template-columns: 4fr 1fr;
        }
        .placeform {
            display: grid;
            grid-template-rows: repeat(10, 1fr);
            margin: 1vw;
        }
    }
    @media screen and (max-width: 960px) {
        .container {
            grid-template-rows: 1fr 1fr;
        }
        .placeform {
            margin: auto;
        }
    }
</style>

<script>
    import Map from '@/components/Map.vue';
    import router from '@/router';
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
                    alert("등록이 완료되었습니다!")
                    router.push('/')
                })
                .catch(e => {
                    console.log(e)
                    if (e.message == "Request failed with status code 401") alert('에러: 장소 등록을 위해선 로그인이 필요합니다.')
                    else alert("오류가 발생했습니다.")
                })
            } else {
                alert("모든 정보를 다 입력해주세요!")
            }
        }
        }
    }
</script>