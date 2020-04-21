const validator = require('validator')
const isEmpty = require('./is-empty.js')
module.exports = function (data) {
    let errors = {}
    data.name = !isEmpty(data.name) ? data.name : '' //校验一下必须是字符串类型不是字符串返回空
    data.email = !isEmpty(data.email) ? data.email : ''
    data.password = !isEmpty(data.password) ? data.password : ''
    data.password2 = !isEmpty(data.password2) ? data.password2 : ''
    if (!validator.isLength(data.name, {
            min: 2,
            max: 30
        })) {
        errors.name = '名字的长度大于2位小于30位'
    }
    if (validator.isEmpty(data.name)) {
        errors.name = '用户名不能为空'
    }
    if (validator.isEmpty(data.email)) {
        errors.email = '邮箱不能为空'
    }
    if (!validator.isEmail(data.email)) {
        errors.email = '邮箱格式不正确'
    }
    if (validator.isEmpty(data.password)) {
        errors.password = '密码不能为空'
    }
    if (!validator.isLength(data.password2, {
            min: 6,
            max: 30
        })) {
        errors.password2 = '密码的长度不能大于6位小于30位'
    }
    if (validator.isEmpty(data.password2)) {
        errors.password2 = '确认密码不能为空'
    }
    if (!validator.equals(data.password, data.password2)) {
        errors.password2 = '密码不一致'
    }
    return {
        errors,
        isVaild: isEmpty(errors)
    }
}