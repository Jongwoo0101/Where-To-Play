<template>
  <!DOCTYPE html>
  <html lang="ko">
  <head>
    <meta charset="UTF-8">
    <title>Where To Play</title>
  </head>
  <body>
    <div id="container">    
      <header>
        <div id="logo">
          <a href="#"><h1>Where To Play</h1></a>
        </div>
        <nav>
          <ul id="topMenu">
            <li><a href="#">회원가입</a></li>
            <li><a href="#">로그인</a></li>
          </ul>
        </nav>
      </header>
      <body>
        <p id="description">Where To Play?</p>
        <h1>#주변 운동장을 쉽게 찾고 싶을 때</h1>
        <h1>#통합된 서비스</h1>
        <h1>#예약 링크까지 바로 이동</h1>
        <button id="start">시작 하기</button>
      </body>
      <footer>    
        <section id="bottomMenu">
          <ul>
            <li><a href="#">About US</a></li>
            <li><a href="#">개인정보처리방침</a></li>
            <li><a href="#">사이트맵</a></li>
          </ul>
        </section>   
      </footer>  
    </div> 
  </body>
  </html>
</template>

<script>

</script>


<style>
* {
  margin:0;   /* 마진 리셋 */
  padding:0;   /* 패딩 리셋 */
  box-sizing: border-box;   /* 박스 영역은 테두리까지 */ 
}
a {
  text-decoration:none;  /* 텍스트 링크 밑줄 없애기 */ 
}
ul {
  list-style: none;
}

#container {
  margin:0 auto;  /* 화면 중앙에 배치 */
  width:100%;    /* 너비 */
}

/*********************************/
/* 헤더 영역 - 로고와 내비게이션 */
/*********************************/

header{
  width:100%;    /*  너비 */
  height:100px;   /* 높이 */ 
  background-color:rgb(71, 110, 169);
  
  
}

/* 로고 */
#logo{ 
  float:left;   /* 왼쪽으로 플로팅 */ 
  width:250px;   /*  너비 */ 
  height:100px;   /* 높이 */
  line-height:100px;  /* 세로로 중간에 맞춤 - 줄간격을 높이 값과 같게 */
  padding-left:20px;  /* 왼쪽에 여백 */
}
#logo h1 {
  font-weight:700;
  font-size:30px;   /* 글자 크기 */
  color:#fff;   /* 글자 색*/
  text-shadow:0 -1px 0 #222;  /* 그림자 색 */
}

#description {
  font-weight: 700;
  font-size: 70px;
}
#start {
  font-weight: 700;
  font-size: 50px;
}
/* 내비게이션 */
nav{  
  float:right;   /* 오른쪽으로 플로팅 */
  width:900px;   /*   너비 */  
  height:100px;   /* 메뉴 영역 높이 */  
  padding-top:40px;  /* 메뉴를 아래로 내리기 위해 */  
}
#topMenu {  
  height:60px; 
}
#topMenu > li {
  float:right;  /* 메뉴 항목을 왼쪽으로 플로팅 */ 
  
  position: relative;  
}
#topMenu > li > a{
  display:block;  /* 링크 텍스트는 블록으로 */ 
  font-size:1.1em;
  color:#fff;  /* 글자 색 */
  font-weight:600;  /* 글자 굵기 */
  padding:20px 60px;  /* 패딩 */ 

}
#topMenu > li > a:hover {
  color:#1fa8f8;
  text-shadow:0 -2px #222;
}




footer{   
  width:100%;   /* 너비 */
  height:100px;  /* 높이 */
  border-top:2px solid #222;
}
#bottomMenu{
  width:100%;
  height:20px;
  margin-left:60px;
}
#bottomMenu ul {
  margin-top:15px;  
}
#bottomMenu ul li{
  float:left;  /* 가로로 배치 */ 
  padding:5px 20px;
  border-right:1px solid #ddd;   /* 항목 오른쪽에 테두리 */ 
}
#bottomMenu ul li:last-child{
  border:none;  /* 마지막 항목에는 오른쪽 테두리 없음 */  
}
#bottomMenu ul li a, #bottomMenu ul li a:visited {  
  font-size:15px;  /* 글자 크기 */ 
  color:#666;   /* 글자 색 */ 
} 
</style>
