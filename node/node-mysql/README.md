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

- passport 是一个中间件 passport-jwt 是检验token 的类似的还有 （passport-local **此中间件是通过session校验数据的**）不可混为一谈

   ```jsx
   // serializeUser 在用户登录验证成功以后将会把用户的数据存储到 session 中
   ```

   passport.serializeUser(function(user, done) {

   console.log(1,user)

   done(null, user);

   });

   ```jsx
   // deserializeUser 在每次请求的时候将从 session 中读取用户对象
   ```

   passport.deserializeUser(function(id, done) {

    console.log(2,id)

    done(null, id);

   });

   这两个是序列化session和反序列化session,如果项目是SPA（单页面应用，用token检验）可以不用session,如果要用一定要加这两个函数，不然会报错。也可以在

   passport.authenticate('jwt', **{ session: false }**)加上这个加粗的字体代码，就不会报错了。

   

- 对于上面两个函数我的理解是，序列化函数在请求进入的时候把数据存到session里，反序列化将数据从session取出存的数据,判断是经过isAuthenticated()函数才调用deserializeUser()函数的。所以这个deserializeUser()函数的作用是，获取存在session中的数据提供给req.user，客户端cookie里面存的是session_id然后拿着session_id找到了session里存着的user.id返回给req.user。

- passport-jwt 和 passport-local 不是一个东西，他俩存数据的地方不是一个，一个靠token存数据，一个靠cookie+session存数据，如果你在passport-jwt里面使用session了，那么你就必须进行session的序列化和反序列化，其实token和session实现的效果是一样的，如果在jwt中使用了token在我看来是冗余的，不用app.use(passport.session())，和在验证的时候加{session:false}之后也是可以在req中调用session的，只不过没通过passport中间件，所以没有限制，所以最后

   # 总结

   -  在passport - jwt 里最好别用session，就算想在req里用session也别用passport 中间件注册，检验的时候一定要写{session:false}
   - 以上是我这次实验的想法（2020-08-20）
   - 个人想法，不太确定对不对，有待改进

- [一个博主的理解]: https://www.jianshu.com/p/1bcf32ebf893

  - https://www.jianshu.com/p/1a2427b6cc92
  - net start mysql  ------------------  net stop mysql
  
  - ```
    mysql -uroot -p
    
    
    
    
    
    ```