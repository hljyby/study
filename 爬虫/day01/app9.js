const express = require('express')

const server = express()


const fs = require('fs')
const url = require('url')
const gbk = require('gbk')
const JSDOM = require('jsdom').JSDOM
const segment = require('segment')

var seg = new segment();

seg.useDefault();
server.listen(8888)


server.get('/getmsg',(req,res)=>{
    console.log(req.query)
    // res.send({str:1})
    
    getUrl(Object.keys(req.query)[0],(data)=>{
        // console.log(data)
        // var html = gbk.toString('utf-8',data)
    
        const Dom = new JSDOM(data)
        var document = Dom.window.document
            // console.log(data)
            var myhtml = document.querySelector('.read-content').innerHTML.replace(/<[^>]+>/g,'')
        // console.log(myhtml)
        var myarr = seg.doSegment(myhtml)
        // console.log(myarr)
        var mydata=[]
        myarr.forEach(v => {
    
            if(v.p != 2048){
                mydata.push(v.w)
            }
    
        });
        var myjson = {}
        mydata.forEach(v=>{
            if(!myjson[v]){
                myjson[v] = 1
            }else{
                myjson[v]++
            }
        })
        var datanumber = []
        for(var i in myjson){
            if(myjson[i]>=3){
                datanumber.push(i)
            }
        }
        // console.log(datanumber)
        res.send({'need':datanumber})
        // console.log(myjson)
        // fs.writeFile('yq.html',data,'utf8',(err)=>{
        //     if(err){
        //         console.log(err)
        //     }
        // })
    })
}
)

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
            var str = ''
            res.on('data',buffer=>{
                arr.push(buffer)
                str+=buffer
            })
            res.on('end',()=>{
                var b = Buffer.concat(arr)
                success(str)
            })

        }else if(res.statusCode == 302 || res.statusCode == 301){

            getUrl(res.headers.location,success)
            return
        }

    })

    req.end()

}

server.use(express.static('./'))