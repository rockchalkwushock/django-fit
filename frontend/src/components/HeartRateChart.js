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
          backgroundColor: [
            '#f87979',
            '#fAF979',
            '#f87909',
            '#f00229'
          ],
          data: this.hrData
        }
      ]
    }, {
      title: {
        display: true,
        fontSize: 16,
        text: 'Calories burned by HR Zone'
      }
    })
  }
}
