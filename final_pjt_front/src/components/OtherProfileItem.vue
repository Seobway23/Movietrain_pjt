<template>
  <div>
    <h1> PROFILE PAGE</h1>

    <p>profile data: {{profile}}</p>
    <p>username: {{profile.username}}</p>
    <p>followers: {{followers}}</p>
    <p>followings:{{followings}}</p>
    <p>posts: {{posts}}</p>
    <p>post_likes: {{post_likes}}</p>
    <!-- <p>{{follow}}</p> -->
    <!-- <p>username: {{profile?.username}}</p>
    <p>image: {{profile?.image}}</p>
    <p>email: {{profile?.email}}</p>
    <p>followers_count: {{profile?.followers_count}}</p>
    <p>following_count: {{profile?.following_count}}</p> -->
    <!-- <h1>{{ userProfile.user.username }}</h1>
    <p>Followers: {{follow}}</p> -->
    
  </div>
</template>

<script>
const API_URL = 'http://127.0.0.1:8000'
import axios from 'axios'

export default {
    name: 'ProfileItem',
        data(){
        return{
            profile: null,
            followers : null,
            followings: null,
            posts : null,
            post_likes : null,
            // follow: null,
            follower_flag : 0,
        }
    },
    created(){
      this.getProfile()
      this.following()
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
        url: `${API_URL}/user/profile/${username}/`,
      })
      .then((res)=>{
        console.log(res)
        this.profile = res.data
        this.followers = res.data.followers.length
        this.followings = res.data.followings.length
        this.posts = res.data.post_set.length
        this.post_likes = res.data.like_posts.length
      })
      .catch((err) => console.log(err))
      },

      follow() {
        const username = localStorage.getItem('username')
        const yourname = this.$route.params.id
        

        axios({
          methods: 'post',
          url: `${API_URL}/user/profile/${username}/${yourname}`,
        })
        .then((res)=>{
          console.log(res)
          // this.follower_flag = res.data.flag
        })
        console.log(username)
        // yourname은 어떻게 할꺼?
      }
    },

}
</script>

<style>

</style>

