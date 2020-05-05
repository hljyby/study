<template>
  <div class="soltBox">
    <slot name="app">
        11111
    </slot>
    <slot></slot>
    <button>{{}}</button>
    <button>{{}}</button>
  </div>
</template>

<script>
export default {
  name: "soltBox",
  data() {
    return {};
  },
  methods: {}
};
</script>

<style scoped>
.soltBox {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(255, 255, 255, 0.7);
  z-index: 9999;
}
</style>