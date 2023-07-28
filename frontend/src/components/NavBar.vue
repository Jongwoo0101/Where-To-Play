<template>
    <div class="navbar">
        <div class="logo">
            <p>logo</p>
        </div>
        <div class="navbar-item">
            <p>메인</p>
            <p>운동장 찾기</p>
            <p>운동장 등록</p>
            <p>테마 지도</p>
        </div>
        <div class="navbar-memberinfo">
            <p>로그인</p>
            <p>회원가입</p>
        </div>
    </div>
</template>

<style>
    @media screen and (max-width: 960px) {
        .navbar div:not(:first-child) {display: none;}
    }
    .navbar {
        display: grid;
        grid-template-columns: 1fr 6fr 1fr;
    }
    .logo {
        margin:auto;
    }
    .navbar-item {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
    }
    .navbar-item > p, .navbar-memberinfo > p {
        display: inline;
    }
    .navbar-memberinfo {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
    }
</style>

<script>
    export default {
        name: "NavBar",

    }
</script>