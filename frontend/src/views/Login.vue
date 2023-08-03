<template>
    <div class="form">
        <input type="text" class="id" v-model="id" required>
        <label class="user-id">ID 또는 Email</label>
        <input type="password" class="pw" v-model="pw" required>
        <label class="user-pw">비밀번호</label>
        <button @click="submit">Login</button>
    </div>
</template>

<style>
.form {
    position: relative;
}

.id {
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

.id:focus, id:valid {
    outline: none;
    border: 1.5px solid #1a73e8;
}

.id:focus ~ .user-id, id:valid ~ .user-id {
    transform: translateY(-50%) scale(0.8);
    background-color: #FFFFFF;
    padding: 0.2em;
    color: #2196f3;
}

.pw {
    border: solid 1.5px #000000;
    border-radius: 1rem;
    background: none;
    padding: 1rem;
    font-size: 1rem;
    color: #000000;
    transition: border 150ms cubic-bezier(0.4, 0, 0.2, 1);
    margin-top: 2rem;
}

.user-pw {
    position: absolute;
    left: 15px;
    top: 5.5rem;
    color: #000000;
    pointer-events: none;
    transform: translateY(1rem);
    transition: 150ms cubic-bezier(0.4, 0, 0.2, 1);
}

.pw:focus, pw:valid {
    outline: none;
    border: 1.5px solid #1a73e8;
}

.pw:focus ~ .user-pw, pw:valid ~ .user-pw {
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