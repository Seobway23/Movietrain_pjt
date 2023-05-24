<template>
  <div>
    <p>{{movie.id}}</p>
    <p>{{movie.title}}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name : 'MoviSearchListItem',
  props: {
    movie: Object,
  },
  created: {
    actionsss(){}
  },
  methods:{
    actionsss(){
    console.log(this.movie)
    }
  }

}
</script>

<style>

</style>