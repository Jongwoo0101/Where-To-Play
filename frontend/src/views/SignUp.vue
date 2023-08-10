<template>
    <div class="form">
        <input type="text" placeholder="아이디" v-model="id" required>
        <input type="password" placeholder="비밀번호" v-model="password" required>
        <input type="email" placeholder="이메일" v-model="email" required>
        <input type="text" placeholder="닉네임" v-model="nickname" required>
        <input type="text" placeholder="이름" v-model="name" required>
        <input type="number" placeholder="전화번호" v-model="phonenumber" required>
        <input type="text" placeholder="인증번호 (이후 구현)">
        <input type="text" placeholder="우선순위 1순위" v-model="priority[0]" required>
        <input type="text" placeholder="우선순위 2순위" v-model="priority[1]" required>
        <input type="text" placeholder="우선순위 3순위" v-model="priority[2]" required>
        <button @click="submit()">제출</button>
    </div>
</template>

<style scoped>
    .form {
        display: grid;
    }
</style>

<script>
    import axios from 'axios'
    export default {
        name: "signup",
        data() {
            return {
            id: '',
            name: '',
            password: '',
            email: '',
            nickname: '',
            phonenumber: '',
            priority: ['', '', '']
            }
        },
        methods: {
            submit() {
                axios.post('http://localhost:8000/auth/register/', {
                    "username": this.id,
                    "nickname": this.nickname,
                    "realname": this.name,
                    "email": this.email,
                    "password": this.password,
                    "phonenumber": this.phonenumber,
                    "first_priority": this.priority[0],
                    "second_priority": this.priority[1],
                    "third_priority": this.priority[2],
                }, {
                headers: {
                    "Content-Type": "application/json"
                }})
                .then( response => {console.log(response)})
                .catch( response => {console.log(response)})
            }
        }
    }
</script>