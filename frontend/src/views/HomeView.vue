<template>
  <div class="home">
    <div class="content is-medium">
      <h2 class="title">Where To Play, Where You Want</h2>
      <p class="subtitle">여러분에게 알맞는 운동장을 실시간으로 확인해보세요!</p>
      <router-link to="/findplace">
        <button class="button custom-button">지금 시작하기</button>
      </router-link>
    </div>
    <p class="footer">Developed by <a href="https://github.com/Jongwoo0101/Where-To-Play">자료구조</a>, Copyright © All rights reserved 2023.</p>
  </div>
</template>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
  background-image: url('@/assets/mainscreen-background.jpg');
  background-size: cover;
  background-position: center;
}

.content {
  text-align: center;
  padding: 2em;
  background-color: rgba(255, 255, 255, 0.8); /* 조금 투명한 백그라운드 추가 */
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.title {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 1rem;
}

.subtitle {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 2rem;
}

.button.custom-button {
  padding: 1rem 2rem;
  font-size: 1.2rem;
  background-color: #ff3860;
  color: #ffffff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

.button.custom-button:hover {
  background-color: #d6004f;
}

.footer {
  color: #ffffff;
  font-size: 0.8rem;
  text-align: center;
  margin-top: 2rem;
}

.footer a {
  color: #ffffff;
  text-decoration: none;
}

.footer a:hover {
  text-decoration: underline;
}
</style>

<script>
export default {
  name: 'HomeView',
}
</script>
