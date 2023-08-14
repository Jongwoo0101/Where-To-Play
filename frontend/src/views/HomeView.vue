<template>
  <div class="home">
    <div class="content is-medium">
      <h2>Where To Play, Where You Want</h2>
      <p>여러분에게 알맞는 운동장을 실시간으로 확인해보세요!</p><br>
      <RouterLink to="/findplace"><button class="button is-link">지금 시작하기</button></RouterLink>
    </div>
    <p style="position: absolute; color: #969696; right: 2em; bottom: 1em; text-align: right;">Developed by 자료구조, Copyright(c) All rights reserved 2023.</p>
  </div>
</template>

<style src="@/assets/bulma.min.css" scoped>
</style>

<script>
export default {
  name: 'HomeView',
  components: {
    
  }
}
</script>
