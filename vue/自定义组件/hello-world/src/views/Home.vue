<template>
  <div class="home">
    <p @click="show">click</p>
  </div>
</template>

<script>
export default {
  name: "Home",
  methods: {
    show() {
      this.$messageBox(
        { title: 123 },
        {
          close() {
            this.title = 11111;
          }
        }
      ).then(res => {
        console.log(res);
      });
    }
  }
};
</script>

<style  scoped>
p {
  color: red;
}
</style>