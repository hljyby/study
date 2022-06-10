const mongoose = require('mongoose')

const Schema = mongoose.Schema

const postsModules = new Schema({
    text: {
        type: String,
        required: true
    },
    user: {
        type: String,
        required: true
    },
    likes: [{
        user: {
            type: Schema.Types.ObjectId,
            ref: 'users'
        }
    }],
    comments: [{
        date: {
            type: Date,
            default: Date.now
        },
        text: {
            type: String,
            required: true
        },
        user: {
            type: Schema.Types.ObjectId,
            ref: 'users'
        }
    }],
    date: {
        type: Date,
        default: Date.now
    }
})


module.exports = Posts = mongoose.model('posts',postsModules)