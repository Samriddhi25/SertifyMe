<template>
  <a v-bind:href="href" v-bind:class="{ active: isActive }" v-on:click="go">
    <slot></slot>
  </a>
</template>

<script>
import routes from "../router";

export default {
  props: {
    href: {
      type: String,
      required: true,
    },
  },
  computed: {
    isActive() {
      return this.href === this.$root.currentRoute;
    },
  },
  methods: {
    go(event) {
      event.preventDefault();
      this.$root.currentRoute = this.href;
      window.history.pushState(null, routes[this.href], this.href);
    },
  },
};
</script>

<style scoped>
.active {
  color: #FFFFFF;
  font-size: 22px;
}

a {
  font-size: 22px;
  color: #8ec2bb;
  text-decoration: none;
  margin: 10px;
}
</style>
