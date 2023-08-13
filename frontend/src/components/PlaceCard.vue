<template>
<div class="card" :id="placeId">
  <div class="card-image">
    <figure class="image is-4by3">
      <img :src="'http://192.168.219.113:8000/'+placeImage">
    </figure>
  </div>
  <div class="card-content">
    <div class="content">
      <p class="title is-4">{{ placeName }}</p>
      <p>{{ placeLocation }}</p>
      <p>{{ placeDescription }}</p>
      <a @click="open()">{{ openDetail }}</a>
      <div class="place-details" v-if="placeDetail">
        별점: {{ ratings }} / 5 <br>
        상태: {{ openStatus.open_status? (openStatus.open_status? "열려있음":"닫힘"):"정보 없음" }}
        <button @click="updateOpenStatus(true)">열렸어요</button><button @click="updateOpenStatus(false)">닫혔어요</button>
        <br>
        - 업데이트 시간: {{ openStatus.status_updated_at? openStatus.status_updated_at: "정보 없음" }} <br>
        연락처: {{ response.contact }}<br>
        홈페이지: <a :href="response.homepage" target="_blank">Link</a><br>
        운영 시간: {{ response.time }}<br><br>
        당신의 별점을 등록하세요!
        <StarRating @update:rating="setRating" :show-rating="false"/>
        <div class="comment-zone">
          <input type="text" v-model="commentBox"><button @click="postcomment()">댓글 등록</button>
            <Comment
            v-for="comment in this.response.comments"
            :username="comment.username"
            :commentValue="comment.comment"
            :created_at="comment.comment_uploaded_at"
            />
          </div>
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
          ratings: '정보 없음',
          placeDetail: false,
          openStatus: false,
          response: null,
          rating: 0,
          openDetail: '상세 정보 열기',
          commentBox: ''
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
          axios.post('http://192.168.219.113:8000/place/rating/'+this.response.id+'/', {
            "user": sessionStorage.getItem('nickname'),
            "rating": this.rating
          })
          .then(res => {
            console.log(res)
            alert("별점 등록 성공")
          })
          .catch(e => {
            console.log(e)
          })
        },
        setRating: function(rating) {
          this.rating = rating;
          this.addRating()
        },
        updateOpenStatus(status) {
          axios.post('http://192.168.219.113:8000/place/open_status/'+this.response.id+'/', {
            "username": sessionStorage.getItem('nickname'),
            "open_status": status
          })
          .then(res => {
            console.log(res)
            alert("상태가 업데이트 되었습니다!")
          })
          .catch(e => {
            console.log(e)
          })
        },
        postcomment() {
          axios.post('http://192.168.219.113:8000/place/comment/'+this.response.id+'/', {
            "username": sessionStorage.getItem('nickname'),
            "comment": this.commentBox
          })
          .then(res => {
            console.log(res)
            alert("댓글 작성이 완료되었습니다!")
          })
          .catch(e => {
            console.log(e)
          })
        }
      },
      mounted() {
        axios
            .get('http://192.168.219.113:8000/place/get/'+this.placeId+'/')
            .then(res => {
              console.log(res.data)
              this.response = res.data
              if (this.response.homepage.search("https://") != 0 && this.response.homepage.search("http://") != 0)
                this.response.homepage = "//" + this.response.homepage
              if (this.response.ratings[0] != null)  {// ratings data가 available하다면 평균 내기
                console.log("result: ", this.response.ratings.length)
                for (let i = 0; i < this.response.ratings.length; i++) {
                  var rate = 0;
                  rate+=this.response.ratings[i].rating
                }
                rate/=this.response.ratings.length
                console.log("[Result of rate]: ", rate)
                this.ratings = rate;
              }
            })
        axios
        .get('http://192.168.219.113:8000/place/open_status/'+this.placeId+'/')
        .then(res => {
          this.openStatus = res.data
        })
      }
    }
</script>