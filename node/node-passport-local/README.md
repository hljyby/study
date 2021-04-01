- 接口一
  - localhost:3000/[page = 1]/?message=[关键词 = sm]
  - page 是页数 message是关键词
  - localhost:3000/1/message=SM
- 接口二
  - localhost:3000/users/del
  - 删除的数据写死了
- PM2 NODE管理工具
  - npm install pm2 -g
  - pm2 list
  - pm2 start ./bin/www --watch
  - pm2 save
  - pm2 startup 
  - 将上面生成的命令，粘贴到控制台进行，搞定。
  - ====================================================================
  - window平台下开机自启不好使，下面是兼容版本
  - npm install pm2-windows-startup -g  
  - pm2-startup install
  - pm2 save
- mysql数据库
  - 用户名：root
  - 密码：1234
- 自己写着玩的，先用python爬虫爬的第一会所的数据，用node 写的后台连的数据库。

- passport passport-jwt jsonwebtoken 这三个是做token 的 

- passport 是一个中间件 passport-jwt 是检验token 的类似的还有 （passport-local 此中间件是通过session校验数据的）不可混为一谈

- passport.serializeUser(function(user, done) {

   console.log(1,user)

   done(null, user);

  });

  

  passport.deserializeUser(function(id, done) {

   console.log(2,id)

   done(null, id);

  });

  这两个是序列化session和反序列化session,如果项目是SPA（单页面应用，用token检验）可以不用session,如果要用一定要加这两个函数，不然会报错。也可以在

  passport.authenticate('jwt', **{ session: false }**)加上这个加粗的字体代码，就不会报错了，不过也用不了session了

  

- 对于上面两个函数我的理解是，序列化函数在请求进入的时候把数据存到session里，反序列化函数在下一个请求进来前，将数据反序列化出去。应该是为了不影响弄得的操作，node 为单线程。

- [一个博主的理解]: https://www.jianshu.com/p/1bcf32ebf893

  