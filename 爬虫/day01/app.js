const http = require('http');
const fs = require('fs');
// console.log(http)
// http.createServer((req,res)=>{
//             res.write('你好');
//             console.log(res)
//             res.end()
// }).listen(4000);

// console.log(fs)
let req = http.request({
    hostname:'pic1.win4000.com',
    path: '/pic/3/bd/41850ec17f.jpg'
},res=>{

    var arr=[];
    var str = '';
    res.on('data',buffer=>{
        arr.push(buffer)
        str += buffer
    })
    res.on('end',()=>{
        var b = Buffer.concat(arr)
        fs.writeFile('zifeng.jpg',b,()=>{
            console.log("成功了")
        })
        // fs.write(fd, buf, function(err, written, buffer) {});
    }
    )
})

req.end()