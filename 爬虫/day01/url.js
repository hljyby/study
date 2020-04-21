const imgurl = 'https://aecpm.alicdn.com/simba/img/TB183NQapLM8KJjSZFBSutJHVXa.jpg'

const url = require('url')

var urlObj = url.parse(imgurl)

console.log(urlObj)