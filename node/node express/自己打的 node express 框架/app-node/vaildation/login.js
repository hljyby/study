const validator = require('validator')
const isEmpty = require('./is-empty.js')
module.exports = function (data) {
    let errors = {}
    //校验一下必须是字符串不是字符串返回空
    data.email = !isEmpty(data.email) ? data.email : ''
    data.password = !isEmpty(data.password) ? data.password : ''


    if (validator.isEmpty(data.email)) {
        errors.name = '邮箱不能为空'
    }
    if (!validator.isEmail(data.email)) {
        errors.name = '邮箱格式不正确'
    }
    if (validator.isEmpty(data.password)) {
        errors.name = '密码不能为空'
    }

    return {
        errors,
        isVaild: isEmpty(errors)
    }
}