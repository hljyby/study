const request = require('request');
async function a() {
    request('https://www.runoob.com/jsref/jsref-gettime.html',function (error ,response, body) {
        // 返回的结果和 GET 一样
        console.log(response)
        var e = new Date();
        console.log(e.getTime() - n)
      })
}


function pro(){
    return new Promise(res=>{
        setTimeout(() => {
            res("asss")
        }, 2000);
    })
}

async function b() {
    let tasks = []
    for (let i = 1; i < 10; i++) {
        pro().then(res=>{
            console.log(res)
            var e = new Date();
            console.log(e.getTime()-n)
        })
        // console.log(c)

    }



    // let c = await a()
    // console.log(c)
    // var e = new Date();
    // console.log(e.getTime() - n)
}
var d = new Date();
var n = d.getTime();
// console.log(n)
b()

