const validator = require('validator')
const isEmpty = require('./is-empty.js')
module.exports = function (data) {
    let errors = {}
    //校验一下必须是字符串不是字符串返回空
    data.handle = !isEmpty(data.handle) ? data.handle : ''
    data.status = !isEmpty(data.status) ? data.status : ''
    data.skills = !isEmpty(data.skills) ? data.skills : ''


    if (!validator.isLength(data.handle, {
            min: 2,
            max: 40
        })) {
        errors.name = '名字的长度大于2位小于40位'
    }

    if (validator.isEmpty(data.handle)) {
        errors.name = 'handle不能为空'
    }

    if (validator.isEmpty(data.status)) {
        errors.name = 'status不能为空'
    }

    if (validator.isEmpty(data.skills)) {
        errors.name = 'skills不能为空'
    }

    if (!isEmpty(data.website)) {
        if (validator.isURL(data.website)) {
            errors.name = 'website格式不正确'
        }
    }
    if (!isEmpty(data.tengxunkt)) {
        if (validator.isURL(data.tengxunkt)) {
            errors.name = 'tengxunkt格式不正确'
        }
    }
    if (!isEmpty(data.wangyikt)) {
        if (validator.isURL(data.wangyikt)) {
            errors.name = 'wangyikt格式不正确'
        }
    }
    return {
        errors,
        isVaild: isEmpty(errors)
    }
}