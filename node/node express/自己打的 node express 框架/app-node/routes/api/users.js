const express = require('express')
const User = require('../../modules/user.js')
const registervalidator = require('../../vaildation/register.js')
const loginvalidator = require('../../vaildation/login.js')
const secretOrKey = require('../../config/keys.js').secretOrKey
const jwt = require('jsonwebtoken');
const passport = require('passport')
const router = express.Router()
const gravatar = require('gravatar');

const svg = require('svg-captcha')

router.get('/test', (req, res) => {
    var captcha = svg.create({
        size:4,
        ignoreChars:'0o1i',
        noise:1,
        color:true ,
    });    
    req.session.captcha = captcha.text.toLowerCase()
    res.type('svg')
    res.send(captcha.data)
})

router.post('/register', (req, res) => {
    const {
        errors,
        isVaild
    } = registervalidator(req.body)
    if (!isVaild) {
        return res.status(400).json(errors)

    }
    User.findOne({
            email: req.body.email
        })
        .then(user => {
            if (user) {
                return res.status(400).json({
                    message: '邮箱已被注册!'
                })
            } else {
                let avatary = gravatar.url(req.body.email, {
                    s: '200',
                    r: 'pg',
                    d: 'mm'
                })

                const newUser = new User({
                    email: req.body.email,
                    name: req.body.name,
                    password: req.body.password,
                    head: avatary
                })
                newUser.save().then(user => {
                    return res.json(user)

                }).catch(err => {
                    throw err
                    // console.log(err)
                })

            }
        })
})

router.post('/login', (req, res) => {
    const {
        errors,
        isVaild
    } = loginvalidator(req.body)
    if (!isVaild) {
        return res.status(400).json(errors)

    }
    User.findOne({
        email: req.body.email
    }).then(user => {
        if (!user) {
            return res.status(404).json({
                msg: '用户不存在'
            })
        }
        if (req.body.password == user.password) {
            let rule = {
                id: user.id,
                email: user.email
            }
            jwt.sign(rule, secretOrKey, {
                expiresIn: 3600
            }, (err, token) => {
                if (err) throw err
                if (token) {
                    return res.json({
                        msg: '登陆成功',
                        type: 1,
                        token: 'Bearer ' + token
                    })
                }
            })

        } else {
            return res.status(400).json({
                msg: '密码不正确'
            })
        }
    })
})


router.get('/current', passport.authenticate('jwt', {
    session: false
}), function (req, res, next) {
    console.log(1)
    req.params = {app:1}
    next()
}, (req, res) => {
    console.log(req.params)
    return res.json({
        msg: req.user
    })
})

// router.get('/appnames', (req, res) => {
//     // console.log(next)
//     res.json({
//         params: req.params,
//         query: req.query
//     })
//     // next()
// })
// router.get('/appnames', (req, res) => {
//     res.json({
//         params: req.params,
//         query: req.query
//     })
// })

module.exports = router