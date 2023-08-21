<template>
    <div class="register">
      <div class="form">
        <p>회원가입</p>
        <input type="text" placeholder="아이디" v-model="id" required>
        <input type="password" placeholder="비밀번호" v-model="password" required>
        <input type="email" placeholder="이메일" v-model="email" required>
        <input type="text" placeholder="닉네임 (최대 12글자)" v-model="nickname" required>
        <input type="text" placeholder="이름" v-model="name" required>
        <div class="input-button">
          <input type="tel" pattern="[0-1]{3}-[0-9]{4}-[0-9]{4}" placeholder="전화번호 (-제외)" v-model="phonenumber" required>
          <button class="send-sms" @click="sendSMS()">인증</button>
        </div>
        <input type="text" placeholder="인증번호 (이후 구현)">
        <dropdown 
            v-for="id in 3"
            :options="optionsList"
            :placeholder="'우선순위 '+id+'순위 (필수)'"
            :selected="priority[id-1]"
            v-on:updateOption="(option) => methodToRunOnSelect(option, id)"/>
        <button class="submit" @click="submit()">제출</button>
      </div>
    </div>
  </template>
  
  <style scoped>
  .register {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-size: cover;
    background-image: url('@/assets/background.jpeg');
  }
  
  .form {
    background-color: rgba(255, 255, 255, 0.9);
    display: grid;
    width: 30vw;
    margin: 3em auto 3em auto;
    padding: 1em 3em 1em 3em;
    border-radius: 0.5rem;
    box-shadow: 0 0.3em 1em 0.1em #a3a3a3;
  }
  
  .form p {
    font-weight: 600;
    font-size: 20pt;
    margin: 1rem 0 1rem;
  }
  
  .form input[type=tel] {
    max-width: 100%;
  }
  
  .form input[type=text], .form input[type=password], .form input[type=tel], .form input[type=email] {
    padding: 1rem;
    margin: 0.5rem;
  }
  
  .input-button {
    display: grid;
    grid-template-columns: 5fr 1fr;
  }
  
  .send-sms {
    border-radius: 5px;
    border: none;
    width: 4.5rem;
    height: 3rem;
    margin: auto;
    color: white;
    background-color: #1e90ff;
    cursor: pointer;
  }
  
  .submit {
    padding: 1rem;
    border-radius: 0.5rem;
    border: 0;
    color: white;
    background-color: #5b92ff;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .submit:hover {
    background-color: #1362ff;
  }
  
  @media screen and (max-width: 960px) {
    .form {
      width: 80vw;
      margin: 10vw auto 10vw auto;
      padding: 5vh 5vw 5vh 5vw;
    }
  }
  </style>
  
  <script>
  import axios from 'axios'
  import dropdown from 'vue-dropdowns';
  import CryptoJS from 'crypto-js'
  export default {
    name: "signup",
    components: {
      'dropdown': dropdown
    },
    data() {
      return {
        id: '',
        name: '',
        password: '',
        email: '',
        nickname: '',
        phonenumber: '',
        priority: ['', '', ''],
        verified: false,
        verifycode: null,
        optionsList: [{name: '#넓은구장'}, {name: '#편리한교통'}, {name: '#최신시설'}, {name: '#깔끔한구장'}, {name: '#작은구장'}, {name: '#저렴한이용'}, {name: '#프리미엄시설'}]
      };
    },
    methods: {
      submit() {
        if (
          this.id != '' &&
          this.name != '' &&
          this.password != '' &&
          this.email != '' &&
          this.nickname != '' &&
          this.phonenumber != '' &&
          this.priority[0] != '' &&
          this.priority[1] != '' &&
          this.priority[2] != ''
        ) {
          if (this.verified) {
            axios
              .post(
                process.env.VUE_APP_BACKEND_ADDRESS + '/auth/register/',
                {
                  username: this.id,
                  nickname: this.nickname,
                  realname: this.name,
                  email: this.email,
                  password: this.password,
                  phonenumber: this.phonenumber,
                  first_priority: this.priority[0],
                  second_priority: this.priority[1],
                  third_priority: this.priority[2],
                },
                {
                  headers: {
                    "Content-Type": "application/json"
                  }
                }
              )
              .then(response => {
                alert("회원가입에 성공했습니다!");
                this.$router.push("/");
              })
              .catch(response => {
                alert("회원가입에 실패했습니다!");
              });
          } else {
            alert("전화번호 인증이 필요합니다!");
          }
        } else {
          alert("모든 정보를 다 입력하세요!");
        }
      },
      sendSMS() {
        if (/^[0-9]{3}-[0-9]{4}-[0-9]{4}$/.test(this.phonenumber)) {
          alert("인증되었습니다");
          this.verified = true;
        } else {
          alert("전화번호를 형식에 맞게 입력하세요");
        }
      },
      methodToRunOnSelect(option, id) {
        this.priority[id] = option.name;
      },
    }
  };
  </script>
  