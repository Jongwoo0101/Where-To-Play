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
            <div class="burger-menu" :class="{ active: isShown, toggle: isActive}" @click="toggle()">
                <div class="burger-bar" :class="{ toggle: isActive }"></div>
                <div class="burger-bar" :class="{ toggle: isActive }"></div>
                <div class="burger-bar" :class="{ toggle: isActive }"></div>
            </div>
        </div>
    </div>
</template>

<style>
    @media screen and (max-width: 960px) {
        .navbar > .navbar-item {display: none;}
        .navbar {
            display: flex;
            justify-content: space-between;
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
            background-color: black;
            margin-top: 5px;
        }
        .burger-bar.toggle {
            
        }
        @keyframes slidein {
            from {
                background-color: black;
                margin-top: 5px;
            }
            to {
                background-color: red;
                margin-top: 5px;
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
            grid-template-columns: repeat(2, 1fr);
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