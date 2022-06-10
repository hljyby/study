const express = require('express')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const passport = require('passport')
var path = require('path');
const session = require('express-session');

const db = require('./config/keys').mongURI
const users = require("./routes/api/users.js")
const profiles = require("./routes/api/profiles.js")
const posts = require("./routes/api/posts.js")
const app = express();

mongoose.connect(db, {
    useUnifiedTopology: true,
    useNewUrlParser: true,
    useFindAndModify: false
}, ).then(() => {
    console.log('数据库连接成功')
}).catch(err => console.log(err))
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));

app.use(session({
    secret: '123456',
    resave: false,
    saveUninitialized: true,
    cookie: {
        secure: true
    }
}))

app.use(bodyParser.urlencoded({
    extended: false
}))
app.use(bodyParser.json())


app.use(passport.initialize());
require('./config/passport')(passport)

app.use('/api/users', users)
app.use('/api/profiles', profiles)
app.use('/api/posts', posts)

const port = process.env.PORT || 5000;


app.listen(port, () => {
    console.log(`Serve is Success for ${port}`)
})