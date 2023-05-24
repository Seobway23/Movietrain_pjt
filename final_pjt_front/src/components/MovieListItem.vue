<template>
  <div>
    <p>{{movie.poster_path}}</p>
    <p>{{movie.title}}</p>
    <!-- <router-link :to="{
      name: 'MovieView',
      params : {id: movie.id}}">
      [DETAIL]
    </router-link> -->
    <hr>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  }

}
</script>

<style>

</style>