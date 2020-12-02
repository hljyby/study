#### 一 .  在项目根目录下新建以下三个文件：

###### .env.development(开发环境)，.env.production(生产环境)，.env.test(测试环境)

1.1 .env.development内代码如下



```csharp
//开发环境配置
NODE_ENV = 'development' 
VUE_APP_MODE = 'development' 
VUE_APP_API_URL = 'http://192.168.1.1:8008/api/'  //url地址根据自己需要自行填写
```

1.2 .env.production内代码如下



```csharp
//生产环境配置
NODE_ENV = 'production'
VUE_APP_MODE = 'production'
VUE_APP_API_URL = 'http://baidu.com/'   //url地址根据自己需要自行填写
```

1.3 .env.test内代码如下



```csharp
//测试环境配置
NODE_ENV = 'production'
VUE_APP_MODE = 'test'
VUE_APP_API_URL = 'http://192.168.8.8:8008/api/'  //url地址根据自己需要自行填写
outputDir = test  
```

### 二  .在项目根目录下新建vue.config.js(必须是此文件名)

#### vue.config.js内代码如下



```java
module.exports = {
   publicPath: "./",
   outputDir: process.env.outputDir
}
```

### 三 . 修改package.json下面scripts配置如下



```cpp
"scripts": {
    "serve": "vue-cli-service serve --open",
    "build": "vue-cli-service build",
    "lint": "vue-cli-service lint",
    "dev": "vue-cli-service serve --open",
    "test": "vue-cli-service build --mode test", //添加此项是为了生成测试环境代码包
    "publish": "vue-cli-service build && vue-cli-service build --mode test"//生成测试环境和正式环境代码包
  },
```

### 四 . 打包命令



```cpp
npm run dev  //开发环境运行
npm  run test   //生成测试环境代码包
npm  run publish  //生成测试环境和正式环境代码包
```

### 五 . 附加vue.config.js默认配置项



```jsx
module.exports = {
     // 基本路径
     publicPath: '/',
     // 输出文件目录
     outputDir: 'dist',
     // eslint-loader 是否在保存的时候检查
     lintOnSave: true,
     // 是否使用包含运行时编译器的Vue核心的构建。
     runtimeCompiler: false,
     // 默认情况下babel-loader忽略其中的所有文件node_modules。
         transpileDependencies: [],
        // 生产环境sourceMap
         productionSourceMap: true,
     // webpack配置
     configureWebpack: () => {},
     chainWebpack: () => {},
     // css相关配置
     css: {
      // 启用 CSS modules
      modules: false,
      // 开启 CSS source maps?
      sourceMap: false,
      // css预设器配置项
      loaderOptions: {},
     },
     // webpack-dev-server 相关配置
 devServer: {
  host: '0.0.0.0',
      port: 8080,
      https: false,
      hotOnly: false,
            proxy: {
                //名字可以自定义，这里我用的是api/
                '/api/': {
                    target: process.env.NODE_ENV == 'production'?'生产环境接口地址':'开发环境接口地址', 
                    //设置你调用的接口域名和端口号 别忘了加https
                    ws: true, // 是否代理websockets
                    changeOrigin: true, //这里设置是否跨域
                    pathRewrite: {
                        '^/api/': 'https://www.163.com'
                    }
                }
            }
        },
     // enabled by default if the machine has more than 1 cores
     parallel: require('os').cpus().length > 1,
     // PWA 插件相关配置
     pwa: {},
     // 第三方插件配置
     plugins: [
            new webpack.ProvidePlugin({
                $: "jquery",
                jQuery: "jquery",
                "windows.jQuery": "jquery"
            })
        ]
}
```