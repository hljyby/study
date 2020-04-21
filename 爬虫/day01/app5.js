const fs = require('fs')
const url = require('url')
const gbk = require('gbk')


getUrl('https://detail.tmall.com/item.htm?spm=a230r.1.14.8.45c559ceEkq3iT&id=602909085750&cm_id=140105335569ed55e27b&abbucket=10&sku_properties=10004:709990523;5919063:6536025',(data)=>{
    // console.log(data)
    var html = gbk.toString('utf-8',data)
    console.log(html)
    // fs.writeFile('taobao.html',data,'utf8',(err)=>{
    //     console.log(11)
    //     if(err){
    //         console.log(err)
    //     }
    // })
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
        console.log(res.statusCode,res.headers.location)
        if(res.statusCode == 302){
            getUrl(res.headers.location,success)
            return
        }
        var arr = []
        res.on('data',buffer=>{
            arr.push(buffer)
        })
        res.on('end',()=>{
            var b = Buffer.concat(arr)
            success(b)
        })
    })

    req.end()

}