<template>
  <div id="app">
    <nav>
      <ul>
        <li><router-link :to="{name: 'HomeView'}">Movies</router-link></li>| 
        <li>
          <router-link :to="{name: 'PostView'}">Community</router-link>|
          <!-- <router-link to="/Post">Community</router-link>  -->
          </li>
        <li>
        <!-- <li v-if="isloggedIn"> -->
          <router-link :to="{ name: 'SignUpView' }">SignUp</router-link> | 
          <router-link :to="{ name: 'LoginView' }">Login</router-link> |
          <router-link :to="{ name: 'ProfileView' }">Profile</router-link> |
        </li>
        <li>
        <!-- <li v-else> -->
          <!-- 로그아웃 누르면 메인으로 가게끔, 라우터링크가 아니라, 함수로 써야함
          함수를 써서, 로그아웃처리하면서, 메인 페이지로 이동하게끔-->
          <!-- postview 이용해서 -> 라우터링크로하지말고, 변수로 할당할 수 있도록 하기 -->
          <!-- <router-link>logout</router-link> |  -->
          <!-- 프로필을 누르면 프로필 화면으로 가게끔 -->
          <!-- <router-link>profile</router-link> |  -->
        </li>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>


<script>
export default {
  data() {
    return {
      isLoggedIn : false, 
    }
  },
  mounted() {
    this.isLoggedIn = true
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
