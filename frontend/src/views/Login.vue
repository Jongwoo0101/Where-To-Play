<template>
    <div class="container">
        <div class="form">
        <input type="text" class="id" v-model="id" autofocus>
        <label class="user-id">ID 또는 Email</label>
        <input type="password" class="pw" v-model="pw">
        <label class="user-pw">비밀번호</label>
        <button @click="submit">Login</button>
        </div>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    
}

.form {
    width: 50%;
    top: 5rem;
    display: grid;
    position: relative;
    background: #FFFFFF;
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

.id:focus, .id:valid {
    outline: none;
    border: 1.5px solid #1a73e8;
}

.id:focus ~ .user-id, .id:valid ~ .user-id {
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

.pw:focus, .pw:valid {
    outline: none;
    border: 1.5px solid #1a73e8;
}

.pw:focus ~ .user-pw, .pw:valid ~ .user-pw {
    transform: translateY(-50%) scale(0.8);
    background-color: #FFFFFF;
    padding: 0.2em;
    color: #2196f3;
}

button {
    border: 0;
    box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
    padding: 1rem;
    border-radius: 1rem;
    transition: background-color 0.5s;
    background-color: azure;
    margin: 1rem 0 0 0;
}

button:hover {
    transition: background-color 0.5s;
    background-color: #1a73e8;
}
</style>

<script>
    import axios from 'axios'
    export default {
        name: "Login",
        data() {
            return {
                id: null,
                pw: null,
            }
        },
        methods: {
            submit() {
                axios.post(process.env.VUE_APP_BACKEND_ADDRESS+"/auth/login/",{
                    "username": this.id,
                    "password": this.pw
                }, {
                    headers: {
                        "Content-Type": "application/json"
                    }
                })
                .then( response => {
                    sessionStorage.setItem('nickname', response.data.nickname.nickname)
                    sessionStorage.setItem('userToken', response.data.token)
                    sessionStorage.setItem('level', response.data.level)
                    this.$router.push("/")
                })
                .catch( response => { alert("로그인 정보를 다시 확인하세요")})
            },
        }
    }
</script>