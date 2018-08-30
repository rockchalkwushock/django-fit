import { Doughnut } from 'vue-chartjs'

export default {
  extends: Doughnut,
  props: ['hrData'],
  mounted: function() {
    this.renderChart({
      labels: ['Out of Range', 'Fat Burn', 'Cardio', 'Peak'],
      datasets: [
        {
          label: 'calories burned',
          backgroundColor: '#f87979',
          data: this.hrData
        }
      ]
    })
  }
}
