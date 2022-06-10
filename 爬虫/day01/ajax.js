function ajax(method,_url,data,fun) {
    // 1、定义一个xhr变量存放ajax对象
    var xhr;
    // 2、当window对象里面存在XMLHttpRequest时
    if (window.XMLHttpRequest) {
        // 实例化一个XMLHttpRequest()构造函数
        xhr = new XMLHttpRequest();
    } else {
        // 为防止一些浏览器中没有XMLHttpRequest
        // 当window对象里面没有XMLHttpRequest时就实例化一个ActiveXObject()构造函数
        xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }

    // 3、使用XHR时要调用open(a1,a2,a3);方法a1:请求类型,a2:请求的url,a3:是否发送异步请求(ture/false)
    xhr.open(method,_url,true);
    
    // 4、send();请求在主体发送的数据
    // 发送请求如果需要发送到服务器的端的数据,那么send(data) ,data:数据 需转换为字符串类型的
    xhr.send(JSON.stringify(data));
    //当readyState值每发生一次变化就调用一次onreadystatechange方法
    xhr.onreadystatechange = function() {
        // readystate为4代表已经接收全部响应数据,并且已经可以在客户端使用
        if (xhr.readyState == 4) {
            // readystate:状态为200时表示请求已经完全成功
            if (xhr.status == 200) {
                // responseText:作为响应主体被返回的文本
                // JSON.parse():将字符串json转换为数组类型的json
                // 把返回的数据responseText从string转换为JSON数据格式并打印出来
                fun(JSON.parse(xhr.responseText));
            }
        }
    }
}


// // 调用封装好的函数
// ajax("get","http://192.168.95.237:81/ajaxapi/public/index.php/api/api/index",null,function(data){
//     document.body.innerHTML=data.code;
// });

// // post提交
// var data={
//     stuid:"1027"
// }
// ajax("post","http://192.168.95.237:81/ajaxapi/public/index.php/api/api/selectuserid",data,function(data){
//     document.body.innerHTML=data.code;
// });


/* 
    注意：
        1、检查提交方式类型：get/post是否和后台一致（该类型接口文档会标注，若一致仍然报错，请与后台再次确认）
        2、检查接口url是否写错
        3、检查接口是否需要传数据到后台，若需上传，便仔细把自己上传的数据和接口文档上对比，
            观察有没有错写、多写、少写，数据格式是否正确（一般和后台人员确认一下要传什么数据格式），观察上传的值是否会出现undefined
        4、若以上都正确了还是报错，那么便让后台人员看看是否是后台程序出错（一般http状态码返回500就是后台程序出错，但是也不排除是前端传递过去的数据不对导致后台报错）
        6、如果出现跨域问题，就找后台解决
 
 */