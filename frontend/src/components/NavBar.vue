<template>
    <nav>
        <div class="navbar">
        <div class="logo">
            <router-link to="/"><img class="logo" src="@/assets/wtp_logo.png"/></router-link>
        </div>
        <div class="navbar-item">
            <router-link to="/"><p class="link">메인</p></router-link>
            <router-link to="/findplace"><p class="link">운동장 찾기</p></router-link>
            <router-link to="/addplace"><p class="link">운동장 등록</p></router-link>
            <router-link to="/thememap"><p class="link">테마 지도</p></router-link>
        </div>
        <div class="navbar-memberinfo" :class="{ loggedIn: isLoggedin }">
            <p v-if="isLoggedin">레벨 {{ level }}</p>
            <p v-if="isLoggedin">{{ nickname }}</p>
            <p class="link" v-if="isLoggedin" @click="logout()">로그아웃</p>
            <router-link to="/login" v-if="!isLoggedin"><p v-if="!isLoggedin" class="login link">로그인</p></router-link>
            <p class="division" v-if="!isLoggedin">|</p>
            <router-link to="/signup" v-if="!isLoggedin"><p v-if="!isLoggedin" class="signin link">회원가입</p></router-link>
            <div class="burger-menu" :class="{ active: isShown, toggle: isActive}" @click="toggle()">
                <div class="burger-bar" :class="{ toggle: isActive }"></div>
                <div class="burger-bar" :class="{ toggle: isActive }"></div>
                <div class="burger-bar" :class="{ toggle: isActive }"></div>
            </div>
        </div>
    </div>
    <div class="mobile-navbar-item" :class="{ toggle: isActive }">
        <router-link to="/findplace"><p class="link">운동장 찾기</p></router-link>
        <router-link to="/addplace"><p class="link">운동장 등록</p></router-link>
        <router-link to="/thememap"><p class="link">테마 지도</p></router-link>
    </div>
    </nav>
</template>

<style scoped>
    img.logo {
        max-width: 100%;
        height: 50px;
    }
    a {
        color: #2c3e50;
        text-decoration: none;
        text-decoration-color: none;
        margin: 0;
        display: flex;
        justify-content: center;
    }
    nav {
        margin: 0 0 10px 0;
        padding: 0;
    }
    .mobile-navbar-item {
        display: none;
    }
    p.link:hover {
        color: rgb(147, 147, 255)
    }
    p.link {
        margin: auto;
    }
    @media screen and (max-width: 960px) { /* grid가 최소 960px을 요구하기에 모바일과 대응 별개로 진행 */
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
        .burger-menu {
            margin: auto;
            padding-left: 10px;
            width: 30px;
            height: 30px;
        }
        .navbar-memberinfo {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
        }
        .navbar-memberinfo > p {
            display: inline;
        }
        .navbar-memberinfo > p.division {
            padding: 0.5px;
            text-shadow: 0.1px black;
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
            justify-content: space-evenly;
        }
        .mobile-navbar-item.toggle > p {
            display: inline;
            margin-left: 5vw;
            margin-right: 5vw;
            margin-top: 0;
            margin-bottom: 0;
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
            grid-template-columns: 1fr 8fr 2fr;
        }
        .logo {
            margin: auto;
        }
        .navbar-item {
            display: grid;
            grid-template-columns: repeat(9, 1fr);
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
            margin-right: 3vw;
        }
        .navbar-memberinfo.loggedIn {
            display: grid;
            margin-right: 3vw;
        }
        .navbar-memberinfo.loggedIn > p {
            margin-right: 0.23rem;
        }
        .navbar-memberinfo > p.division {
            padding: 4.5px;
            text-shadow: 0.1px black;
        }
    }
</style>

<script>
    import axios from 'axios'
    export default {
        name: "NavBar",
        data() {
            return {
                isLoggedin: false,
                isActive: false,
                isShown: false,
                nickname: '',
                level: '0'
            }
        },
        updated() {
            this.checkLogin()
        },
        mounted() {
            this.checkLogin()
        },
        created() {
            this.checkLogin()
            window.addEventListener("resize", this.showMenu);
        },
        destroyed() {
            window.removeEventListener("resize", this.showMenu);
        },
        methods:{
            checkLogin() {
                if (sessionStorage.getItem("userToken") != null) {
                    this.isLoggedin = true;
                    this.nickname = sessionStorage.getItem('nickname')
                    this.level = sessionStorage.getItem('level')
                } else
                    this.isLoggedin = false;
            },
            toggle() {
                this.isActive = !this.isActive
            },
            showMenu() {
                if (window.innerWidth <= 960) {
                    this.isShown = true;
                }
            },
            logout() {
                axios.post(process.env.VUE_APP_BACKEND_ADDRESS + '/auth/logout/',
                    {},
                    { headers : { Authorization: 'Token '+sessionStorage.getItem('userToken') }},
                )
                .then(res => {
                    console.log(res)
                    sessionStorage.removeItem('userToken');
                    sessionStorage.removeItem('username');
                    sessionStorage.removeItem('level');
                    this.$forceUpdate();
                })
                .catch(e => {
                    console.log(e)
                })
            }
        }
    }
</script>