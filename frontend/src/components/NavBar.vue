<template>
    <nav>
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
            <p class="login">로그인</p>
            <p>|</p>
            <p class="signin">회원가입</p>
            <div class="burger-menu" :class="{ active: isShown, toggle: isActive}" @click="toggle()">
                <div class="burger-bar" :class="{ toggle: isActive }"></div>
                <div class="burger-bar" :class="{ toggle: isActive }"></div>
                <div class="burger-bar" :class="{ toggle: isActive }"></div>
            </div>
        </div>
    </div>
    <div class="mobile-navbar-item" :class="{ toggle: isActive }">
        <p>운동장 찾기</p>
        <p>운동장 등록</p>
        <p>테마 지도</p>
    </div>
    </nav>
</template>

<style>
    nav {
        margin: 0;
        padding: 0;
    }
    .mobile-navbar-item {
        display: none;
    }
    .navbar-memberinfo:hover > p:first-child {
        color: rgb(147, 147, 255)
    }
    .navbar-memberinfo:hover > p:nth-child(3) {
        color: rgb(147, 147, 255)
    }
    @media screen and (max-width: 960px) {
        p {
            font-size: 11pt;
        }
        .navbar > .navbar-item {display: none;}
        .navbar {
            display: flex;
            justify-content: space-between;
        }
        .navbar-item.toggle > p:first-child {
            display: none;
        }
        .logo > p {
            margin-top: 15px;
            margin-bottom: 15px;
        }
        .navbar-memberinfo > p {
            display: inline;
            padding-left: 20px;
        }
        .burger-menu {
            margin: auto;
            width: 30px;
            height: 30px;
        }
        .navbar-memberinfo {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
        }
        .burger-bar {
            width: 30px;
            height: 3px;
            border-radius: 0.5px;
            box-shadow: 1px 1px rgb(171, 171, 171);
            animation: 0.5s bluetoblack;
            background-color: black;
            margin-top: 5px;
        }
        .burger-bar.toggle {
            animation: 0.5s blacktoblue;
            background-color: rgb(111, 111, 255);
        }
        .mobile-navbar-item.toggle {
            display: flex;
            justify-content: center;
        }
        .mobile-navbar-item.toggle > p {
            display: inline;
            margin-left: 15px;
            margin-right: 15px;
            margin-top: 0px;
            margin-bottom: 0px;
        }
        @keyframes blacktoblue {
            from {
                background-color: black;
            }
            to {
                background-color: rgb(111, 111, 255);
            }
        }
        @keyframes bluetoblack {
            from {
                background-color: rgb(111, 111, 255);
            }
            to {
                background-color: black;
            }
        }
    }
    @media screen and (min-width: 960px) {
        .navbar {
            display: grid;
            grid-template-columns: 1fr 6fr 1fr;
        }
        .logo {
            margin: auto;
        }
        .navbar-item {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
        }
        .navbar-item > p, .navbar-memberinfo > p {
            display: inline;
        }
        .burger-menu {
            display: none;
        }
        .navbar-memberinfo {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
        }
        .navbar-memberinfo > p:nth-child(2) {
            padding: 4.5px;
            text-shadow: 0.1px black;
        }
    }
</style>

<script>
    export default {
        name: "NavBar",
        data() {
            return {
                isActive: false,
                isShown: false
            }
        },
        created() {
            window.addEventListener("resize", this.showMenu);
        },
        destroyed() {
            window.removeEventListener("resize", this.showMenu);
        },
        methods:{
            toggle() {
                this.isActive = !this.isActive
            },
            showMenu() {
                if (window.innerWidth <= 960) {
                    this.isShown = true;
                }
            }
        }
    }
</script>