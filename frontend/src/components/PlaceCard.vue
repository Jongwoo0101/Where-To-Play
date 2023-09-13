<template>
  <div class="card" :id="placeId">
    <div class="card-image">
      <figure class="image is-4by3">
        <img :src="this.backend_url+placeImage">
      </figure>
    </div>
    <div class="card-content">
      <div class="content">
        <p class="title is-4">{{ placeName }}</p>
        <p>{{ placeLocation }}</p>
        <p class="place-rating">별점: {{ ratings }} / 5</p>
        <a @click="open()">{{ openDetail }}</a>
        <div class="place-details" v-if="placeDetail">
          <div class="place-description">
            장소 소개:<br>
            {{ placeDescription }}
          </div>
          상태: {{ openStatus.status_updated_at? (openStatus.open_status? "열려있음":"닫힘"):"정보 없음" }}
          <button style="background-color: #23C55D; border: 0;" @click="updateOpenStatus(true)">열렸어요</button><button style="background-color: #F84F31; border: 0;" @click="updateOpenStatus(false)">닫혔어요</button>
          <br>
          <p style="font-size: 8pt; color: #aaaaaa; text-align: right;">업데이트 시간: {{ openStatus.status_updated_at? openStatus.status_updated_at: "정보 없음" }}</p>
          연락처: {{ response.contact }}<br>
          홈페이지: <a :href="response.homepage" target="_blank">Link</a><br>
          운영 시간: {{ response.time }}<br>
          <p style="font-weight: 500; margin-top: 1em; font-size: 14pt;">별점을 등록하세요!</p>
          <StarRating style="justify-content: center;" @update:rating="setRating" :show-rating="false"/>
          <div class="comment-zone">
            <div class="post-comment" style="position: relative;">
              <input type="text" style="width: 100%; height: 1.7rem;" v-model="commentBox">
              <button style="position: absolute; top: 0; right: 0.1px; margin-top: 0.2rem;" @click="postcomment()">댓글 등록</button>
            </div>
            <div class="display-comments">
              <Comment
              v-for="comment in this.response.comments.slice().reverse()"
              :place_id="this.placeId"
              :comment_id="comment.id"
              :username="comment.username"
              :commentValue="comment.comment"
              :created_at="comment.comment_uploaded_at"
              /> 
            </div>
          </div>
          <div class="subimage-zone">
            <p>장소 세부 이미지</p>
            <input style="padding: 3px; border-radius: 3px; border: 1px solid #8b8b8b; margin: 4px;" @change="getImage" type="file" accept="image/*">
            <button @click="uploadImage">업로드하기</button>
            <div class="subimage-container">
              <img v-if="!this.response.sub_images[0]" src="@/assets/unavailable-image.jpg">
              <img v-for="datas in this.response.sub_images" :src="this.backend_url+datas.image">
            </div>
          </div>
          <p style="text-align: right; padding-top: 0.5rem; color:#aaaaaa;" @click="fixdata">정보 수정하기</p>
          </div>
      </div>
    </div>
  </div>
  </template>
  
  <style src="@/assets/bulma.min.css" scoped>
  </style>
  
  <script>
    import axios from 'axios';
    import StarRating from 'vue-star-rating'
    import Comment from '@/components/Comment.vue'
      export default {
        name: 'PlaceCard',
        components: {
          StarRating,
          Comment
        },
        props: {
          placeId: '',
          placeImage: null,
          placeName: "장소 이름",
          placeLocation: "장소 위치",
          placeDescription: "장소 설명",
        },
        data() {
          return {
            backend_url: '',
            ratings: '정보 없음',
            placeDetail: false,
            openStatus: false,
            response: null,
            rating: 0,
            openDetail: '상세 정보 열기',
            commentBox: '',
            image: null,
            key: 0
          }
        },
        methods: {
          open() {
            if (this.placeDetail === false) {
              this.placeDetail = true
              this.openDetail = '상세 정보 닫기'
            } else {
              this.placeDetail = false
              this.openDetail = '상세 정보 열기'
            }
          },
          addRating() {
            axios.post(process.env.VUE_APP_BACKEND_ADDRESS+'/place/rating/'+this.response.id+'/', {
              "user": sessionStorage.getItem('nickname'),
              "rating": this.rating
            },
            { headers : { Authorization: 'Token '+sessionStorage.getItem('userToken') }}
            )
            .then(() => {
              this.reloadData()
              setTimeout(() => {
                var rate = 0;
                for (let i = 0; i < this.response.ratings.length; i++) {
                  rate+=this.response.ratings[i].rating
                }
                rate/=this.response.ratings.length
                this.ratings = rate;
              }, 500)
            })
            .catch(e => {
              alert("해당 기능은 로그인 후 사용 가능합니다.")
            })
          },
          setRating: function(rating) {
            this.rating = rating;
            this.addRating()
          },
          updateOpenStatus(status) {
            axios.post(process.env.VUE_APP_BACKEND_ADDRESS+'/place/open_status/'+this.response.id+'/', {
              "username": sessionStorage.getItem('nickname'),
              "open_status": status
            },
            { headers : { Authorization: 'Token '+sessionStorage.getItem('userToken') }})
            .then(res => {
              axios.get(process.env.VUE_APP_BACKEND_ADDRESS+'/place/open_status/'+this.placeId+'/')
              .then(res => {
                this.openStatus = res.data
              })
              alert("상태가 업데이트 되었습니다!")
            })
            .catch(e => {
              alert("해당 기능은 로그인 후 사용 가능합니다.")
            })
          },
          postcomment() {
            if (this.commentBox != '') {
              axios.post(process.env.VUE_APP_BACKEND_ADDRESS+'/place/comment/'+this.response.id+'/', {
              "username": sessionStorage.getItem('nickname'),
              "comment": this.commentBox
              }, { headers : { Authorization: 'Token '+sessionStorage.getItem('userToken') }})
              .then(res => {
                this.commentBox = ''
                this.reloadData()
              })
              .catch(e => {
                alert("해당 기능은 로그인 후 사용 가능합니다.")
              })
            } else {
              alert("댓글을 입력해주세요!")
            }
          },
          getImage(imageFile) {
            this.image = imageFile.target.files[0]
          },
          uploadImage() {
            const formData = new FormData()
            if (this.image)
              formData.append('image', this.image)
            formData.append('username', sessionStorage.getItem('nickname'))
            axios.post(process.env.VUE_APP_BACKEND_ADDRESS+"/place/image/"+this.response.id+'/', 
              formData,
              { headers: { 'Content-Type': 'multipart/form-data', Authorization: 'Token '+sessionStorage.getItem('userToken') } }
            )
            .then(res => {
              this.reloadData()
              alert("등록이 완료되었습니다!")
            })
            .catch(e => {
              if (e.message == "Request failed with status code 401") alert("해당 기능은 로그인 후 사용 가능합니다.")
              else alert("이미지를 등록해주세요!")
            })
          },
          reloadData() {
            axios.get(process.env.VUE_APP_BACKEND_ADDRESS+'/place/get/'+this.response.id+'/')
            .then(res => {
              this.response = res.data
            })
          },
          fixdata() {
            this.$router.push("/adjustplace/"+this.response.id)
          }
        },
        mounted() {
          this.backend_url = process.env.VUE_APP_BACKEND_ADDRESS
          axios
              .get(process.env.VUE_APP_BACKEND_ADDRESS+'/place/get/'+this.placeId+'/')
              .then(res => {
                this.response = res.data
                if (this.response.homepage.search("https://") != 0 && this.response.homepage.search("http://") != 0)
                  this.response.homepage = "//" + this.response.homepage
                if (this.response.ratings[0] != null)  {// ratings data가 available하다면 평균 내기
                  var rate = 0;
                  for (let i = 0; i < this.response.ratings.length; i++) {
                    rate+=this.response.ratings[i].rating
                  }
                  rate/=this.response.ratings.length
                  this.ratings = rate;
                }
              })
          axios
          .get(process.env.VUE_APP_BACKEND_ADDRESS+'/place/open_status/'+this.placeId+'/')
          .then(res => {
            this.openStatus = res.data
          })
        }
      }
  </script>