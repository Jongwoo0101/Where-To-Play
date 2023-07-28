<template>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Where To Play</title>
  <link rel="stylesheet" href="./mpstyle.css">
</head>
<body>
  <header>
    <div class="logo-menu-container">
      <div class="logo">
        <h1>Where To Play</h1> <!-- 로고 텍스트 -->
      </div>
      <nav>
        <ul>
          <!-- Your menu items go here -->
          <li><a href="#">메인</a></li>
          <li><a href="#">운동장 찾기</a></li>
          <li><a href="#">운동장 등록</a></li>
          <li><a href="#">테마지도</a></li>
        </ul>
      </nav>
    </div>
    <div class="user-menu">
      <a href="#">로그인</a> <!-- 로그인 링크 -->
      <span class="divider">|</span> <!-- 세로 막대 -->
      <a href="#">회원가입</a> <!-- 회원가입 링크 -->
    </div>
  </header>
  <!-- The rest of your website content goes here -->
</body>
</html>

</template>

<script>

</script>

<style>
/* styles.css */
body {
  margin: 0;
  padding: 0;
}

header {
  background-color: black; /* 상단 바 색깔 */
  color: white; /* 글자 색깔 */
  display: flex;
  justify-content: space-between; /* 로고와 메뉴, 로그인/회원가입 메뉴 간격 자동 조정 */
  align-items: center;
  padding: 10px;
  height: 80px; /* 상단 바 높이를 80px로 조정 */
}

.logo-menu-container {
  display: flex;
  align-items: center;
}

.logo {
  margin-right: 200px; /* 로고와 메뉴 사이 간격을 30px로 조정 */
  margin-left: 30px;
}

.logo h1 {
  margin: 0; /* 로고 텍스트의 기본 여백 제거 */
  color: white; /* 로고 텍스트 색상 설정 */
  font-size: 30px; /* 로고 텍스트 크기를 24px로 조정 */
}

nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

nav ul li {
  display: inline;
  margin-right: 120px; /* 메뉴 항목 사이 간격을 10px로 조정 */
}

nav ul li:last-child {
  margin-right: 0; /* 마지막 메뉴 항목 오른쪽 간격 제거 */
}

nav ul li a {
  color: white; /* 메뉴 항목 글자 색깔 */
  text-decoration: none;
  font-size: 20px; /* 메뉴 항목 글자 크기를 18px로 조정 */
}

.user-menu {
  display: flex;
  align-items: center;
}

.user-menu a {
  color: white;
  text-decoration: none;
  font-size: 15px; /* 로그인/회원가입 메뉴 글자 크기를 18px로 조정 */
  margin-right: 10px;
}

.divider {
  color: white;
  margin-right: 10px; /* 세로 막대(|)와 로그인/회원가입 메뉴 사이 간격 조정 */
}

</style>
