const fs = require('fs')
const url = require('url')


getUrl('https://aecpm.alicdn.com1244314',(data)=>{
    fs.writeFile('taobao.jpg',data,(err)=>{
        if(err){
            console.log(err)
        }
    })
})

function getUrl(sUrl,success){
    var urlObj = url.parse(sUrl)
    if(urlObj.protocol == 'https:'){
        var http = require('https')
    }
    if(urlObj.protocol == 'http:'){
        var http = require('http')
    }

    var req = http.request({
        hostname:urlObj.hostname,
        path:urlObj.path
    },res=>{
        var arr = []
        res.on('data',buffer=>{
            arr.push(buffer)
        })
        res.on('end',()=>{
            var b = Buffer.concat(arr)
            success && success(b)
        })
    })

    req.end()
    req.on('error',()=>{
        console.log("404了")
    })
}