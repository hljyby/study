# vue 自定义 api 管理

```javascript
/*
 * @Description: api aixos的二次封装  request.js
 * @Version: 2.0
 * @Autor: lhl
 * @Date: 2020-07-14 16:12:35
 * @LastEditors: lhl
 * @LastEditTime: 2020-08-20 17:08:27
 */
import Vue from 'vue';
import axios from 'axios';
import store from '../store/index'
import qs from 'qs'; // axios自带模块 若报错找不到重新安装即可

// 全局的 axios 默认值
// axios.defaults.baseURL = 'https://api.example.com';
// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';


// 使用自定义配置新建一个 axios 实例
const instance = axios.create({
  baseURL: 'api', // process.env.BASE_API, // api的 base_url
  timeout: 100000, // 10s 请求超时时间
  // headers: 'xx'
})

// 请求拦截器(全局)
// Authorization-token: xxx-token
instance.interceptors.request.use(config => {
  console.log(config, '请求拦截器')
  const token = store.state.user.token;  
  // console.log(token,'token请求拦截器')
  // const token = 'xxx-token';
  token && (config.headers['Authorization-token'] = token);
  config.withCredentials = true
  if (config.headers['Content-Type'] === 'application/json') {
    config.data = JSON.stringify(config.data)
  }
  if (config.headers['Content-Type'] === 'multipart/form-data') {
    return config
  }
  if (config.method === 'post' || config.method === 'put' || config.method === 'delete') {
    if (typeof (config.data) !== 'string') {
      config.data = qs.stringify(config.data)
    }
  }
  return config
}, error => {
  return Promise.reject(error)
})

// 响应拦截器(全局)
instance.interceptors.response.use(response => {
  console.log(response, '响应拦截器')
  // 把axios的data层去掉原本（res.data.xx） 直接使用数据就可以res.xx即可
  return response.data
}, error => {
  return Promise.reject(error)
})


export default instance

// 使用axios在调用后台接口超时或是报某个特性的错误码时，需要重新发送请求。此时用到一个第三方的库：axios-retry解决了这个问题

// npm install axios-retry

// import axiosRetry from 'axios-retry';

// //配置axios
// axiosRetry(axios, { 
//     retries: 3,  //设置自动发送请求次数
//     retryCondition: (error)=>{
//         //true为打开自动发送请求，false为关闭自动发送请求
//         //这里的意思是当请求方式为get时打开自动发送请求功能
//         return (error.config.method === 'get');
//     }
// });
```



```javascript
/*
 * @Description: 所有api的入口文件 index.js 将来 main.js 引入挂载 vue原型上面 方便统一管理无需各种 import
 * @Version: 2.0
 * @Autor: lhl
 * @Date: 2020-07-20 10:18:58
 * @LastEditors: lhl
 * @LastEditTime: 2020-08-20 17:12:26
 */ 

// import * as xxx from 'xxx'; 会将若干export导出的内容组合成一个对象返回；
// import xxx from 'xxx';（export default xxx）只会导出这个默认的对象作为一个对象


import * as user from './user'
import * as infoList from './infoList'

export default {
  user,
  infoList
}
// 假设调用则在组件里面 模块下面的对应的接口方法即可完成调用
// this.$http.user.xx()
// this.$http.infoList.xx()
```



```javascript
/*
 * @Description: 测试列表接口 infoList.js
 * @Version: 2.0
 * @Autor: lhl
 * @Date: 2020-08-03 15:58:10
 * @LastEditors: lhl
 * @LastEditTime: 2020-08-20 17:08:36
 */
import instance from './request'
import store from '../store/index'

// 角色管理列表
export function roleList (data) {
  return instance({
    url: '/systemdata/role/pageList',
    method: 'post',
    headers: { 'Content-Type': 'application/json' },
    data
  })
}
```



```javascript
/*
 * @Description: 用户信息接口 user.js
 * @Version: 2.0
 * @Autor: lhl
 * @Date: 2020-08-03 15:35:51
 * @LastEditors: lhl
 * @LastEditTime: 2020-08-20 17:11:13
 */
import instance from './request'
import store from '../store/index'

// responseType: 'blob', 如果返回的格式是流文件需要加上相应类型

// get请求  
// export function getLoawList(params) {
//   return request({
//     url: '/system/lowlist',
//     method: 'get',
//     params: params
//   })
// }

// 获取用户信息
export function userInfo(data) {
    return instance({
        url: '/user/userInfo/getByLoginUser',
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        data
    })
}

// 获取页面按钮权限
export function btnList (data) {
  return instance({
    url: '/system/menu/getCurrUserButton',
    method: 'post',
    headers: { 'Content-Type': 'application/json' },
    data
  })
}
```