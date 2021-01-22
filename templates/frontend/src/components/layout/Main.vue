<template>
  <div>
    <div class="container">
      <div class="company">SertifyMe</div>
      <div class="menu">
        <router-link
          to="/"
          class="styleLink"
          >Home</router-link
        >
        <router-link
          to="/create"
          class="styleLink"
          >Create</router-link
        >
        <router-link
          to="/template"
          class="styleLink"
          >Template</router-link
        >
      </div>
    </div>
    <slot></slot>
    <div>
      <Credits />
    </div>
  </div>
</template>

<script>
import Credits from "./Credits";
export default {
  components: {
    Credits,
  },
};
</script>

<style scoped>
.container {
  max-width: 100vw;
  background: #243734;
  display: flex;
  padding: 5px;
  justify-content: space-between;
}
.company {
  color: #c6e6e4;
  margin-left: 10px;
  font-weight: bold;
  font-size: 46px;
}
.menu {
  display: flex;
  justify-content: center;
  align-items: center;
}

.styleLink {
  font-size: 22px;
  color: #8ec2bb;
  text-decoration: none;
  margin: 10px;
}
.router-link-exact-active {
  color: #ffffff;
  font-size: 22px;
}
</style>
