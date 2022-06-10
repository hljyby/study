//极简的实现+链式调用+延迟机制+状态
class Promise {
    callbacks = [];
    state = 'pending'; //增加状态
    value = null; //保存结果
    constructor(fn) {
        fn(this._resolve.bind(this));
    }
    then(onFulfilled) {
        if (this.state === 'pending') { //在resolve之前，跟之前逻辑一样，添加到callbacks中
            this.callbacks.push(onFulfilled);
        } else { //在resolve之后，直接执行回调，返回结果了
            onFulfilled(this.value);
        }
        return this;
    }
    _resolve(value) {
        this.state = 'fulfilled'; //改变状态
        this.value = value; //保存结果
        this.callbacks.forEach(fn => fn(value));
    }
}