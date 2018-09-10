<template>
  <footer>
    <p v-if="date > 2018">© 2018 - {{date}} Cody Brunner</p>
    <p v-else>© {{date}} Cody Brunner</p>
    <p class="meta">Built with
      <img src="../assets/logo.png" alt="VueJS">
    </p>
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
.meta {
  align-items: center;
  display: flex;
  margin: 0;
}
.meta img {
  height: 40px;
}
</style>
