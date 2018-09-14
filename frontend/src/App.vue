<template>
  <div id="app">
    <app-header />
    <div v-if="error" class="main">
      <error :msg="message" />
    </div>
    <div v-else-if="userLoading" class="main">
      <dash
        :calories="calories"
        :distance="distance"
        :floors="floors"
        :steps="steps"
        :units="units"
        :user="user"
      />
      <heart-rate-chart v-if="hrData.length > 0" :hr-data="hrData" />
      <bar-chart
        v-if="weekLoading"
        :color="'#2AAe50'"
        :data="caloriesGraph"
        :labels="labels"
        :title="'Calories burned'"
        :units="'calories'"
      />
      <bar-chart
        v-if="weekLoading"
        :color="'#200e50'"
        :data="distanceGraph"
        :labels="labels"
        :title="'Distance traveled'"
        :units="'kilometers'"
      />
      <bar-chart
        v-if="weekLoading"
        :color="'#2c3550'"
        :data="floorsGraph"
        :labels="labels"
        :title="'Floors climbed'"
        :units="'floors'"
      />
      <bar-chart
        v-if="weekLoading"
        :color="'#9c3e50'"
        :data="stepsGraph"
        :labels="labels"
        :title="'Steps taken'"
        :units="'steps'"
      />
      <div v-else>
        <spinner
          size='huge'
          line-fg-color='#3cb371'
          message='Please sync your device'
        />
      </div>
    </div>
    <div v-else class="main">
      <h2 class="shameless-plug">Welcome to Django Fit, a prettier alternative to seeing your Fitbit data! Written in Django 2.0, Vue 2.5, and ChartsJS.</h2>
      <login class="animated pulse" />
    </div>
    <app-footer />
  </div>
</template>

<script>
import axios from 'axios'
import Spinner from 'vue-simple-spinner'

import AppFooter from './components/Footer'
import AppHeader from './components/Header'
import Dash from './components/Dash'
import Error from './components/Error'
import Login from './components/Login'
import { BarChart, HeartRateChart } from './components'

export default {
  name: 'App',
  components: {
    AppFooter,
    AppHeader,
    Dash,
    Error,
    Login,
    HeartRateChart,
    BarChart,
    Spinner
  },
  data() {
    return {
      calories: null,
      caloriesGraph: null,
      distance: null,
      distanceGraph: null,
      error: false,
      floors: null,
      floorsGraph: null,
      hrData: [],
      hrLoading: false,
      labels: null,
      message: '',
      steps: null,
      stepsGraph: null,
      weekLoading: false,
      units: '',
      user: {},
      userLoading: false
    }
  },
  mounted: function() {
    try {
      axios
        .get('/api/get_profile')
        .then(res => {
          if (res.data === 'Too Many Requests') {
            this.message = 'Fitbit is being a pain, try back later'
            this.error = true
          }
          this.units = res.data.distance_unit
          this.user.age = res.data.age
          this.user.avatar = res.data.avatar
          this.user.heightUnit = res.data.height_unit
          this.user.name = res.data.full_name
          this.user.weightUnit = res.data.weight_unit
          if (this.user.heightUnit === 'en_US') {
            this.user.height = Math.round(res.data.height * 0.393701)
          } else if (this.user.heightUnit === 'METRIC') {
            this.user.height = res.data.height
          }
          if (this.user.weightUnit === 'en_US') {
            this.user.weight = Math.round(res.data.weight * 2.20462)
          } else if (this.user.weightUnit === 'METRIC') {
            this.user.weight = res.data.weight
          }
          this.userLoading = true
        })
        .catch(error => console.log(error))
      axios
        .get('/api/get_today')
        .then(res => {
          if (res.data === 'Too Many Requests') {
            this.message = 'Fitbit is being a pain, try back later'
            this.error = true
          }
          // Data only seems to exist for Fitbit Blaze.
          if (res.data.heart_rate) {
            res.data.heart_rate.map(hr => {
              this.hrData.push(hr.calories_out)
            })
          }
            this.calories = res.data.calories_out
            this.floors = res.data.floors
            this.steps = res.data.steps
            if (this.units === 'en_US') {
              this.distance = Math.round(res.data.distance * 0.621371)
            } else if (this.units === 'METRIC') {
              this.distance = res.data.distance
            }
            this.hrLoading = true
        })
        .catch(error => console.log(error))
      axios
        .get('/api/get_last_week')
        .then(res => {
          if (res.data === 'Too Many Requests') {
            this.message = 'Fitbit is being a pain, try back later'
            this.error = true
          }
          this.caloriesGraph = res.data.calories
          this.distanceGraph = res.data.distance
          this.floorsGraph = res.data.floors
          this.labels = res.data.labels
          this.stepsGraph = res.data.steps
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
.main {
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: 60vh;
}
.shameless-plug {
  padding-bottom: 2rem;
  width: 50%;
}
</style>
