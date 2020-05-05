<template>
  <div class="about">
    <soltBox v-if="show">
      <p>{{user.age}}</p>
      <p>111</p>
      <p>111</p>
      <p>111</p>
      <p>111</p>
      <p>111</p>
      <p>111</p>
      <p>111</p>
      <p>111</p>
      <p>111</p>
      <p>111</p>
      <template #app>123</template>
    </soltBox>
  </div>
</template>

<script>
import soltBox from "@/components/JS/SoltBox";

export default {
  data() {
    return {
      show: true,
      user: {
        name: "yby",
        age: 12
      }
    };
  },
  methods: {
    hideBlack() {
      this.show = false;
      console.log(this.show);
    }
  },
  components: {
    soltBox
  }
};
</script>
