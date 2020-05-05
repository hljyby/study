// pages/wuui_demo/wuui_demo.js

Page({

  data: {
    theme: '',
  },
  themeChanged(theme) {
    this.setData({
      theme,
    });
  },
  onLoad() {
    const app = getApp();
    this.themeChanged(app.globalData.theme);
    app.watchThemeChange(this.themeChanged);
  },
  onUnload() {
    getApp().unWatchThemeChange(this.themeChanged);
  }
})