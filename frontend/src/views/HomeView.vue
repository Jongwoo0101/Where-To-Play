<template>
  <div class="home">
    <div class="content is-medium">
      <h2>반갑습니다, WhereToPlay입니다.</h2>
      <p>당신에게 알맞는 운동장을 실시간으로 확인해보세요!</p>
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
