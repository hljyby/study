$(function(){
    console.log(123)
    $.getScript('app2.js',function(){
        sayHello1();
    })
    // $.getScript('app2.js').complete(function(){
    //     sayHello2()
    // })
    console.log(456)
})

// 123
// 456
// Helllo sayHello1