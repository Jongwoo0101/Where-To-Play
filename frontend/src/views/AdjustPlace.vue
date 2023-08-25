<template>
    <div class="container">
        <Map @place="getInfo"/>
        <div class="placeform">
            <p>장소 정보 수정</p>
            <label for="file">{{ fileLabel }}</label>
            <input @change="uploadImage($event)" id="file" type="file" accept="image/*">
            <input v-model="placeName" type="text" placeholder="장소명(필수)">
            <input v-model="placeAddress" type="text" placeholder="위치(필수, 지도 클릭시 지정)" disabled>
            <input v-model="placeContact" type="text" placeholder="연락처(선택)">
            <input v-model="placeHomepage" type="text" placeholder="홈페이지(선택)">
            <input v-model="placeTime" type="text" placeholder="운영시간(선택)">
            <textarea v-model="placeDescription" placeholder="여기는 어떤 장소인지 설명해주세요!(선택)"></textarea>
            <legend><input type="checkbox">[선택] 개인정보 수집 및 이용 동의</legend>
            <button @click="submit()">장소 정보 변경</button>
        </div>
    </div>
</template>

<style scoped>
    .placeform {
        height: 80vh;
        overflow: scroll;
    }
    p {
        font-weight: 700;
        font-size: 16pt;
        text-align: center;
        margin: 0;
        padding: 0;
        height: fit-content;
    }
    .file-form {
        border: 3px solid #999999
    }
    label {
        text-align: center;
        margin: auto;
        padding: 10px 50px 10px 50px;
        border: solid 2px #999999;
        border-radius: 5px;
    }
    label:hover {
        border: solid 2px #1a73e8;
    }
    input[type="file"] {
        position: absolute;
        width: 0;
        height: 0;
        padding: 0;
        overflow: hidden;
        border: 0;
    }
    .placeform > input[type=text],textarea {
        display: block;
        margin: 1vh auto auto auto;
    }
    .container {
        margin: auto;
        padding: 1rem;
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
        margin: 10px;
        padding: 15px;
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
            grid-template-columns: 60vw 25vw;
            width: 85vw;
            height: 80vh;
            border-radius: 10px;
            box-shadow: 0px 8px 15px rgba(123, 123, 123);
            overflow: hidden;
        }
        .placeform {
            margin: auto;
            width: 20vw;
            display: grid;
        }
        .placeform > input[type="text"],input[type="file"],textarea {
            margin: 10px;
        }
    }
    @media screen and (max-width: 960px) {
        .container {
            grid-template-rows: 50vh 50vh;
        }
        .placeform {
            margin: auto;
        }
        p {
            margin: 20px;
        }
        .placeform > input[type="text"],input[type="file"],textarea {
            margin: 20px;
        }
    }
</style>

<script>
    import Map from '@/components/Map.vue'
    import axios from 'axios';
    export default {
        name: "AdjustPlace",
        components: {
            Map,
        },
        data() {
            return {
                placeID: null,
                placeAddress: null,
                placeLocation: null,
                image: null,
                placeName: '',
                placeContact: '',
                placeHomepage: '',
                placeTime: '',
                placeDescription: '',
                fileLabel: '메인 사진 업로드'
            }
        },
        methods: {
            getInfo(location) {
                this.placeLocation = location[0];
                this.placeAddress = location[1];
            },
            uploadImage(imageFile) {
                this.image = imageFile.target.files[0];
                this.fileLabel = this.image.name;
            },
            submit() {
                if ((this.placeAddress != null)&&
                     (this.placeLocation != null)&&
                     (this.placeName != null)
                    )
                {
                let date = new Date().toJSON();
                const position = this.placeLocation.split(', ');
                const formData = new FormData()
                if (this.image)
                    formData.append('image', this.image)
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
                formData.append('uploader', sessionStorage.getItem('nickname'))
                axios.post(process.env.VUE_APP_BACKEND_ADDRESS+"/place/adjust/"+this.placeID+'/', 
                    formData
                    ,{ headers: { 'Content-Type': 'multipart/form-data', Authorization: 'Token '+sessionStorage.getItem('userToken')}
                })
                .then(() => {
                    alert("등록이 완료되었습니다!")
                    this.$router.push("/findplace")
                })
                .catch((e) => {
                    if (e.message == "Request failed with status code 401") alert('에러: 장소 등록을 위해선 로그인이 필요합니다.')
                    else alert("오류가 발생했습니다.")
                })
            } else {
                alert("모든 정보를 다 입력해주세요!")
            }
        }
        },
        beforeMount() {
            this.placeID = this.$route.params.placeID
        },
        mounted() {
            axios.get(process.env.VUE_APP_BACKEND_ADDRESS+'/place/get/'+this.placeID+'/')
            .then((res) => {
                this.placeName = res.data.name
                this.placeLocation = res.data.lat+', '+res.data.lng
                this.placeAddress = res.data.address
                this.placeContact = res.data.contact
                this.placeHomepage = res.data.homepage
                this.placeTime = res.data.time
                this.placeDescription = res.data.description
            })
        }
    }
</script>