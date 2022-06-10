<template>
  <div
    class="messageBox"
    :class="{blue:type == 1,gray:type == 2,green:type == 3,isshow:isShow}"
    v-show="isShow"
  >
    <p>{{title}}</p>
    <div class="close" @click="close">
      <i></i>
    </div>
  </div>
</template>

<script>
export default {
  name: "messageBox",
  data() {
    return {
      isShow: false,
      title: "测试",
      type: 1
    };
  },
  methods: {
    close() {
      this.isShow = false;
      console.log(this.type);
    }
  }
};
</script>

<style scoped>
.messageBox {
  position: absolute;
  top: 100px;
  right: 10px;
  width: 0;
  height: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  transition: all 0.5s ease-in;
}
.isshow {
  width: 200px;
}
.close {
  width: 10px;
  height: 10px;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  background: hotpink;
}
.blue {
  background: blue;
}
.gray {
  background: gray;
}
.green {
  background: green;
}
</style>