import MessageBox from './MessageBox'
import SoltBox from './SoltBox'
import Vue from 'vue'

export const messageBox = function (data, methods) {
    return new Promise((res) => {
        let myMessageBox = Vue.extend(MessageBox)
        let vm = new myMessageBox({
            el: document.createElement('div'),
            data: data,
            methods: methods
        }).$mount()
        document.body.appendChild(vm.$el);
        vm.close = function () {
            res()
        }
        Vue.nextTick(() => {
            vm.isShow = true
            // isShow 和弹窗组件里的isShow对应，用于控制显隐
        })
    })

}

export const soltBox = function (template) {

    return new Promise((res) => {
        let mySoltBox = Vue.extend(SoltBox)
        let vm = new mySoltBox({
            el: document.createElement('div'),
            template:template
        }).$mount()
        vm.hideBlack = function () {
            res()
            document.body.removeChild(vm.$el);
        }
        Vue.nextTick(() => {
            document.body.appendChild(vm.$el);
        })
    })

}