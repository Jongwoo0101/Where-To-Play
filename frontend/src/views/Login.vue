<template>
    <div class="form">
        <input type="text" class="input" required>
        <label class="user-id">ID 또는 Email</label>
        <input type="password" v-model="pw" placeholder="PW" required>
        <button @click="submit">Login</button>
    </div>
</template>

<style>
.form {
    position: relative;
}

.input {
    border: solid 1.5px #000000;
    border-radius: 1rem;
    background: none;
    padding: 1rem;
    font-size: 1rem;
    color: #000000;
    transition: border 150ms cubic-bezier(0.4, 0, 0.2, 1);
}

.user-id {
    position: absolute;
    left: 15px;
    color: #000000;
    pointer-events: none;
    transform: translateY(1rem);
    transition: 150ms cubic-bezier(0.4, 0, 0.2, 1);
}

.input:focus, input:valid {
    outline: none;
    border: 1.5px solid #1a73e8;
}

.input:focus ~ label, input:valid ~ label {
    transform: translateY(-50%) scale(0.8);
    background-color: #FFFFFF;
    padding: 0.2em;
    color: #2196f3;
}

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