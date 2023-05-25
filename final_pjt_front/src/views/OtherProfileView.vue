<template>
  <div>
    <OtherProfileItem/>
  </div>
</template>

<script>
import OtherProfileItem from '@/components/OtherProfileItem.vue'

export default {
  name: 'ProfileView',
  components: {
    OtherProfileItem,
  },
  // data(){
  //   return {
  //     otherprofile: null,
  //   }
  // },
  created(){
    this.getOtherProfile()
  },
  methods:{
    getOtherProfile(){
      console.log(this.$route.params.user)
      this.$store.state.$community_id = this.$route.params.user
      console.log(this.$store.state.$community_id)

    }
  }



}
</script>

<style>

</style>