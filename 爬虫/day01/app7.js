const fs = require('fs')
const url = require('url')
const gbk = require('gbk')
const JSDOM = require('jsdom').JSDOM


getUrl('https://item.jd.com/100008306558.html',(data)=>{
    // console.log(data)
    var html = gbk.toString('utf-8',data)

    const Dom = new JSDOM(html)
    var document = Dom.window.document
        console.log(html)
    // console.log(document.querySelector('#page_origin_price').innerHTML)
    
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
        if(res.statusCode == 200){
            var arr = []
            res.on('data',buffer=>{
                arr.push(buffer)
            })
            res.on('end',()=>{
                var b = Buffer.concat(arr)
                success(b)
            })

        }else if(res.statusCode == 302 || res.statusCode == 301){

            getUrl(res.headers.location,success)
            return
        }

    })

    req.end()

}