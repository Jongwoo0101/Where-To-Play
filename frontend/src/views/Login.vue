<template>
    <div class="login-container">
      <div class="login-form">
        <h2>로그인</h2>
        <div class="input-group">
          <input type="text" class="input-field" v-model="id" autofocus required>
          <label class="input-label">ID or Email</label>
        </div>
        <div class="input-group">
          <input type="password" class="input-field" v-model="pw" required>
          <label class="input-label">Password</label>
        </div>
        <button @click="submit">Login</button>
      </div>
    </div>
</template>
  
<style scoped>
.login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f2f2f2;
    background-image: url('@/assets/background.jpeg');
}
  
.login-form {
    width: 400px;
    padding: 2rem;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
}
  
.login-form h2 {
    font-size: 24px;
    margin-bottom: 1rem;
    text-align: center;
}
  
.input-group {
    position: relative;
    margin-bottom: 1.5rem;
}
  
.input-field {
    width: 100%;
    padding: 10px;
    border: none;
    border-bottom: 1px solid #ccc;
    font-size: 16px;
    background-color: transparent;
    transition: border-color 0.3s ease;
}
  
.input-label {
    position: absolute;
    top: 0;
    left: 0;
    font-size: 16px;
    color: #999;
    pointer-events: none;
    transition: transform 0.3s ease, font-size 0.3s ease, color 0.3s ease;
}
  
.input-field:focus,
.input-field:valid {
    outline: none;
    border-color: #1a73e8;
}
  
.input-field:focus ~ .input-label,
.input-field:valid ~ .input-label {
    transform: translateY(-120%) scale(0.75);
    font-size: 12px;
    color: #1a73e8;
}
  
button {
    width: 100%;
    padding: 12px;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    color: #ffffff;
    background-color: #1a73e8;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
  
button:hover {
    background-color: #0e59b3;
}

</style>
  
<script>
  import axios from 'axios';
  export default {
    name: "Login",
    data() {
      return {
        id: "",
        pw: ""
      };
    },
    methods: {
      submit() {
        axios
          .post(
            process.env.VUE_APP_BACKEND_ADDRESS + "/auth/login/",
            {
              username: this.id,
              password: this.pw
            },
            {
              headers: {
                "Content-Type": "application/json"
              }
            }
          )
          .then(response => {
            sessionStorage.setItem("nickname", response.data.nickname.nickname);
            sessionStorage.setItem("userToken", response.data.token);
            sessionStorage.setItem("level", response.data.level);
            this.$router.push("/");
          })
          .catch(response => {
            alert("로그인 정보를 다시 확인하세요");
          });
      }
    }
  };
</script>
  