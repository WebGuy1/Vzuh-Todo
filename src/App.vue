<template>
  <div id="app">
    <div class="container py-2">
      <navigation />


      <todoBlock
        v-bind:todos="todos"
      />


    </div>
  </div>
</template>

<script>

import navigation from '@/components/navigation.vue'
import todoBlock from '@/components/todoBlock.vue'

export default {
  name: 'App',
  data () {
    return {
      todos: [
        {id: 1, msg: "Suck"},
        {id: 2, msg: "my"},
        {id: 3, msg: "dick"}
      ]
    }
  },
  components: {
   navigation,
    todoBlock
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
  margin-top: 60px;
}
</style>
