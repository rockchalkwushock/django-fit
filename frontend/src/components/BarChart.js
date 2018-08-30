import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  props: ['color', 'data', 'labels', 'units'],
  mounted: function() {
    this.renderChart({
      labels: this.labels,
      datasets: [
        {
          label: this.units,
          data: this.data,
          backgroundColor: this.color
        }
      ]
    })
  }
}
