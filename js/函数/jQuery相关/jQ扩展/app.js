// 替换$符号($不再起作用)
var ProsperLee = $.noConflict()

// var $ = ProsperLee;

ProsperLee.sayHello1 = ()=>{
    console.log(123)
}

ProsperLee.fn.sayHello2 = function(){ // this 指向div
    console.log(this)
    ProsperLee(this).text("Hello World!!!")
}

ProsperLee.fn.sayHello3 = (dom) => { // this 指向window
    console.log(this)
    ProsperLee(dom).text("Hello World!!!")
}
var obj = {
    a: ProsperLee.fn.sayHello3
}
obj.b = ProsperLee.fn.sayHello3;

ProsperLee(function(){
    ProsperLee.sayHello1();
    ProsperLee('div').sayHello2() // this 指向div
    ProsperLee('p').sayHello3('p') // this 指向window
    obj.a('a') // this 指向window
    obj.b('a') // this 指向window
})



