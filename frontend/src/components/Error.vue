<template>
  <h1>{{msg}}</h1>
</template>

<script>
export default {
  name: 'Error',
  props: ['msg']
}
</script>

<style>
h1 {
  color: mediumseagreen;
  font-size: 2rem;
}
</style>
