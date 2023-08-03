<template>
    <div class="form">
        <input type="text" v-model="id" placeholder="ID 또는 Email" required>
        <input type="password" v-model="pw" placeholder="PW" required>
        <button @click="submit">Login</button>
    </div>
</template>

<style>

</style>

<script>
    import axios from 'axios'
    export default {
        name: "Login",
        data() {
            return {
                id: '',
                pw: '',
            }
        },
        methods: {
            submit() {
                axios.post("http://localhost:8000/auth/login/",{
                    "username": this.id,
                    "password": this.pw
                }, {
                    headers: {
                        "Content-Type": "application/json"
                    }
                })
                .then( response => {
                    console.log(response.data)
                    sessionStorage.setItem('username', response.data.username)
                    sessionStorage.setItem('userToken', response.data.token)
                    this.$router.push("/")
                })
                .catch( response => {console.log(response), alert("로그인 정보를 다시 확인하세요")})
            },
        }
    }
</script>