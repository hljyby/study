var express = require('express');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var session = require('express-session');
// var swig = require('swig');
// var user = require('./modules/user');
var app = express();
var path = require('path');



//设置swig模板方法;
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
// app.set('views', __dirname + '/views');

//console.log(user)
app.use(session({
  secret: 'hubwiz app', //secret的值建议使用随机字符串
  saveUninitialized: true,
  //此处的cookie设置需要注意;
  cookie: {
    secure: false
  } // 过期时间（毫秒）
}));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieParser());


//引入插件并配置;

var passport = require('passport')
  , LocalStrategy = require('passport-local').Strategy;


app.use(passport.initialize());
app.use(passport.session());
passport.use('local', new LocalStrategy(
  function (username, password, done) {
    var user = {
      id: '1',
      username: '123',
      password: '123'
    };

    if (username !== user.username) {
      return done(null, false, { message: 'Incorrect username.' });
    }
    if (password !== user.password) {
      return done(null, false, { message: 'Incorrect password.' });
    }
    //验证成功后,传入后面的流程；
    return done(null, user);
  }
));

passport.serializeUser(function (user, done) {
  //此处设置session中保存用户的信息,这里保存ID；
  console.log('serializeUser',user)
  done(null, user.id);
});

passport.deserializeUser(function (user, done) {
  console.log('deserializeUser',user)
  done(null, user);
});

app.get('/users',function(req,res){
  console.log(req.session)
  res.send("ok");
});

app.get('/',function(req,res){
  console.log(req.session)
  res.send("fail");
});


app.get('/login', function (req, res) {
  res.render('index', {title: 'index'});
});


//登录入口验证;前面配置的数据处理流,在这里传入验证函数里面；用户信息会保存在session里，并标记登录状态;
app.post('/login', passport.authenticate('local', {
    successRedirect: '/users',
    failureRedirect: '/'
  }),function(req,res){
    console.log('--------------------------')
  console.log(req.body);
});


app.get('/logout', function (req, res) {
  req.logout();
  res.redirect('/');
});

//登录验证函数;通过此函数验证用户是否登录;
function isLoggedIn(req, res, next) {
  if (req.isAuthenticated())
    return next();
  console.log(req.session);
  res.send("未登录");
}


app.get("/app",isLoggedIn,function(req,res){
  console.log(req.session);
  res.send("登录app");
});


app.listen(8080);