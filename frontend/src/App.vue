<template>
  <div id="app">
    <img src="./assets/logo.png">
    <HelloWorld/>
    <heart-rate-chart v-if="this.hrData.length !== 0" :hr-data="hrData" />
    <div v-else>
      <h2>Please sync your fitbit device</h2>
    </div>
    <a href="login/fitbit">Login using Fitbit</a>
  </div>
</template>

<script>
import axios from 'axios'
import HelloWorld from './components/HelloWorld'
import HeartRateChart from './components/HeartRateChart'

export default {
  name: 'App',
  components: {
    HelloWorld,
    HeartRateChart
  },
  data() {
    return {
      hrData: []
    }
  },
  mounted: function() {
    try {
      axios
        .get('/api/get_today')
        .then(res => {
          console.log(res.data)
          if (res.data.heart_rate) {
            res.data.heart_rate.map(hr => {
              this.hrData.push(hr.calories_out)
            })
          }
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
