<template>
  <div class="grid">
    <div class="user">
      <img :src="user.avatar" alt="profile picture">
      <div class="meta">
        <p>{{user.name}} {{user.age}}</p>
        <p v-if="user.heightUnit === 'METRIC' && user.weightUnit === 'METRIC'">{{user.height}}cm {{user.weight}}kg</p>
        <p v-else>{{user.height}}in {{user.weight}}lbs</p>
      </div>
    </div>
    <div class="box steps">{{steps}} steps</div>
    <div class="box floors">{{floors}} floors</div>
    <div class="box calories">{{calories}} calories</div>
    <div v-if="units === 'METRIC'" class="box distance">{{distance}} km</div>
    <div v-else class="box distance">{{distance}} mi</div>
  </div>
</template>

<script>
export default {
  name: 'Dash',
  props: ['calories', 'distance', 'floors', 'steps', 'units', 'user']
}
</script>

<style scoped>
.grid {
  display: grid;
  grid-gap: 10px;
  grid-template-areas:
    'user user'
    'steps calories'
    'floors distance';
  padding: 1rem;
}
.box {
  background-color: mediumseagreen;
  box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);
  font-size: 2rem;
  padding: 1rem;
}
.steps {
  grid-area: steps;
}
.floors {
  grid-area: floors;
}
.calories {
  grid-area: calories;
}
.distance {
  grid-area: distance;
}
.user {
  align-items: center;
  display: flex;
  grid-area: user;
  justify-content: space-evenly;
  padding: 1rem;
}
img {
  border-radius: 50%;
}
p {
  font-size: 1.2rem;
}
</style>
