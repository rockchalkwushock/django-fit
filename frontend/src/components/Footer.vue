<template>
  <footer>
    <p v-if="date > 2018">© 2018 - {{date}} Cody Brunner</p>
    <p v-else>© {{date}} Cody Brunner</p>
  </footer>
</template>

<script>
export default {
  name: 'App-Footer',
  data() {
    return {
      date: new Date().getFullYear()
    }
  }
}
</script>

<style scoped>
footer {
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>
