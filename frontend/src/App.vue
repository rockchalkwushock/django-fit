<template>
  <div id="app">
    <img src="./assets/logo.png">
    <HelloWorld/>
    <a href="login/fitbit">Login using Fitbit</a>
  </div>
</template>

<script>
import axios from 'axios'
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  mounted: function() {
    try {
      console.log('mounted')
      axios
        .get('/api/get_current_activity')
        .then(res => {
          console.log(res.data)
        })
        .catch(error => console.log(error))
    } catch (error) {
      throw error
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
