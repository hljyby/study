class Promise {
    callbacks = []
    state = "pending"
    value = null
    constructor(fn) {
        fn(this._resolve.bind(this))
    }
    then(onFulfilled) {
        return new Promise(resolve => {
            this._handle({
                onFulfilled: onFulfilled || null,
                resolve: resolve
            });
        });
    }
    _handle(callback) {
        console.log(callback)
        if (this.state === 'pending') {
            this.callbacks.push(callback);
            return;
        }
        //如果then中没有传递任何东西
        if (!callback.onFulfilled) {
            callback.resolve(this.value);
            return;
        }
        var ret = callback.onFulfilled(this.value);
        callback.resolve(ret);
    }
    _resolve(value) {
        if (value && (typeof value === 'object' || typeof value === 'function')) {
            var then = value.then;
            if (typeof then === 'function') {
                then.call(value, this._resolve.bind(this));
                return;
            }
        }
        this.state = 'fulfilled'; //改变状态
        this.value = value; //保存结果
        this.callbacks.forEach(callback => this._handle(callback));
    }
}


 var p = new Promise((resolve) => {
    setTimeout(() => {
        resolve({a:1,b:2})
    }, 3000)
}).then(res => {
    console.log(res)
    setTimeout(()=>{
        return res.a
    },2000)
}).then(app=>{
    console.log(app)
})