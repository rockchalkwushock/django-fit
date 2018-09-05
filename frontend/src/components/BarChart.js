import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  props: ['color', 'data', 'labels', 'title', 'units'],
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
    }, {
      title: {
        display: true,
        fontSize: 16,
        text: this.title
      }
    })
  }
}
