const fs = require('fs')
const url = require('url')
const gbk = require('gbk')
const JSDOM = require('jsdom').JSDOM


getUrl('https://detail.tmall.com/item.htm?spm=a230r.1.14.33.14f81b15WzpUz7&id=550007408252&ns=1&abbucket=10',(data)=>{
    // console.log(data)
    var html = gbk.toString('utf-8',data)

    const Dom = new JSDOM(html)
    var document = Dom.window.document
        
    console.log(document.querySelector('.tm-count').innerHTML
    )
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