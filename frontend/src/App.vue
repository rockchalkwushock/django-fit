<template>
  <div id="app">
    <img src="./assets/logo.png">
    <HelloWorld/>
    <bar-chart v-if="weekLoading" :color="'#2AAe50'" :data="calories" :labels="labels" :units="'calories'" />
    <bar-chart v-if="weekLoading" :color="'#200e50'" :data="distance" :labels="labels" :units="'kilometers'" />
    <bar-chart v-if="weekLoading" :color="'#2c3550'" :data="floors" :labels="labels" :units="'floors'" />
    <bar-chart v-if="weekLoading" :color="'#9c3e50'" :data="steps" :labels="labels" :units="'steps'" />
    <heart-rate-chart v-if="hrLoading" :hr-data="hrData" />
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
import BarChart from './components/BarChart'

export default {
  name: 'App',
  components: {
    HelloWorld,
    HeartRateChart,
    BarChart
  },
  data() {
    return {
      calories: null,
      distance: null,
      floors: null,
      hrData: [],
      hrLoading: false,
      labels: null,
      steps: null,
      weekLoading: false
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
            this.hrLoading = true
          }
        })
        .catch(error => console.log(error))
      axios
        .get('/api/get_last_week')
        .then(res => {
          console.log(res.data)
          this.calories = res.data.calories
          this.distance = res.data.distance
          this.floors = res.data.floors
          this.labels = res.data.labels
          this.steps = res.data.steps
          this.weekLoading = true
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
