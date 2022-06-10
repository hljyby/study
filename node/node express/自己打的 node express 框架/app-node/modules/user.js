const mongoose = require('mongoose')
const url = require('url')

const Schema = mongoose.Schema // (架构)

const usersModules = new Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true
    },
    password: {
        type: String,
        required: true
    },
    avatar: {
        type: String,
        default: url.resolve('http://localhost:5000/update/', 'app.jpg')
    },
    head: {
        type: String,
    },
    date: {
        type: Date,
        default: Date.now
    },
})

module.exports = User = mongoose.model('users', usersModules)