import Vue from "vue"
import Router from "vue-router"

import routes from "./common/config/router.js"

Vue.use(Router)

let router = new Router({ routes })

// 全局前置守卫
router.beforeEach((to, from, next) => {
	// 获取token
	let token = window.sessionStorage.getItem('token')
	let user = window.sessionStorage.getItem('user')
	if(token){ // 已登录
		// 防止重复登录
		if(to.path === '/login'){
			Vue.prototype.$message.error('请不要重复登录');
			return next({name:from.name ? from.name : 'index'})
		}
		// 其他验证...
		if(to.name !== 'error_404'){
			// 超级管理员跳过验证
			if(user){
				user = JSON.parse(user)
				if(user.super === 1){
					return next()
				}
			}
			// 验证
			let rules = window.sessionStorage.getItem('rules')
			rules = rules ? JSON.parse(rules) : []
			
			let index = rules.findIndex(item=>{
				return item.rule_id > 0 && item.desc === to.name
			})
			if(index === -1){
				Vue.prototype.$message.error('你没有权限')
				return next({name:from.name ? from.name : 'error_404'})
			}
		}
		next();
	} else {
		// 跳过登录页验证
		if(to.path === '/login'){
			return next();
		}
		// 未登录
		Vue.prototype.$message.error('请先登录');
		next({ path:'/login' })
	}
})

export default router