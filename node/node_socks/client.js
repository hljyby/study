// 这个只是链接tcp 数据的 不是socks5 客户端
// socks5客户端 直接和server服务端一个在本地一个在服务器上 实现ss功能
// 大体功能是 本地请求连接到客户端然后客户端想服务器发起请求实现socks5 功能
// 在浏览器上可以使用SwitchyOmage实现客户端的代理
// 具体怎么实现客户端不太清楚


var net = require('net');

// 指定连接的tcp server ip，端口
var options = {
    host : '192.168.0.103',  
    port : 8888
}

var tcp_client = net.Socket();

// 连接 tcp server
tcp_client.connect(options,function(){
    console.log('connected to Server');
    tcp_client.write('I am tcp_client of node!');
})

// 接收数据
tcp_client.on('data',function(data){
    console.log('received data: %s from server', data.toString());
})

tcp_client.on('end',function(){
    console.log('data end!');
})

tcp_client.on('error', function () {
    console.log('tcp_client error!');
})