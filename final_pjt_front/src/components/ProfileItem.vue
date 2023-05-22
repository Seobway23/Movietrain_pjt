<template>
  <div>
    <h1> PROFILE PAGE</h1>
    <p>username: {{username}}</p>
    <p>image: {{image}}</p>
    <p>email: {{email}}</p>
    <p>last_name: {{last_name}}</p>
    <p>first_name: {{first_name}}</p>

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ProfileItem',
    created() {
        this.getProfile()
    },
    data(){
        return{
            username: null,
            image: null,
            email: null,
            last_name: null,
            first_name: null,
        }
    },
    methods: {
        getProfile() {
          // const username = res.data.username

            axios({
                method: 'get',
                url: `${API_URL}/user/1/`,
                // 이걸 어떻게 알지?
            })
            .then((res) =>{
                this.username = res.data.username
                this.image = res.data.image
                this.email = res.data.email
                this.last_name = res.data.last_name
                this.first_name = res.data.first_name

            })
            .catch((err) => console.log(err))
        }
    }
}
</script>

<style>

</style>

