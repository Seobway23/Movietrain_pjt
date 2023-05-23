<template>
  <div>
    <h1> PROFILE PAGE</h1>
    <p>username: {{profile?.username}}</p>
    <p>image: {{profile?.image}}</p>
    <p>email: {{profile?.email}}</p>
    <p>last_name: {{profile?.last_name}}</p>
    <p>first_name: {{profile?.first_name}}</p>
  </div>
</template>

<script>
const API_URL = 'http://127.0.0.1:8000'
import axios from 'axios'

export default {
    name: 'ProfileItem',
    created(){
      this.getProfile()
    },
    data(){
        return{
            profile: null
        }
    },
    computed: {
      isLogin() {
      return this.$store.getters.isLogin //로그인 여부
    }
    },
    methods:{
      getProfile(){
        const username = localStorage.getItem('username')
      console.log(username)
      axios({
        method: 'get',
        url: `${API_URL}/user/profile/${username}`,
      })
      .then((res)=>{
        console.log(res)
        this.profile = res.data
      })
      .catch((err) => console.log(err))
      }
    },

}
</script>

<style>

</style>

