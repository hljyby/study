/**
 * 规则：
 * 一、例如：index/index，shop/index以index结尾的，path和name默认去除index
 * 二、例如：shop/list，默认生成name为shop_list（如果结尾为index，例如shop/index则是shop）
 * 三、填写后不会自动生成
 * **/
let routes = [
	{
		path:'/',
		name:'layout',
		redirect:{name:'index'},
		component:'layout',
		children:[
			{
				meta:{title:'后台首页'},
				component:'index/index'
			},
			{
				meta:{title:'商品列表'},
				component:'shop/goods/list'
			},
			{
				meta:{title:'创建商品'},
				component:'shop/goods/create'
			},
			{
				meta:{title:'修改商品详情'},
				component:'shop/goods/content'
			},
			{
				meta:{title:'媒体设置'},
				component:'shop/goods/banner'
			},
			{
				meta:{title:'商品属性'},
				component:'shop/goods/attr'
			},
			{
				meta:{title:'商品规格'},
				component:'shop/goods/sku'
			},
			{
				meta:{title:'相册管理'},
				component:'image/index'
			},
			{
				meta:{title:'分类管理'},
				component:'shop/category/list'
			},
			{
				meta:{title:'商品规格管理'},
				component:'shop/sku/list'
			},
			{
				meta:{title:'商品类型管理'},
				component:'shop/type/list'
			},
			{
				meta:{title:'商品评论管理'},
				component:'shop/comment/list'
			},
			{
				meta:{title:'发票管理'},
				component:'order/invoice/list'
			},
			{
				meta:{title:'售后服务'},
				component:'order/after-sale/list'
			},
			{
				meta:{title:'订单列表'},
				component:'order/order/list'
			},
			{
				meta:{title:'会员列表'},
				component:'user/user-list/list'
			},
			{
				meta:{title:'会员等级'},
				component:'user/user-level/list'
			},
			{
				meta:{title:'基础设置'},
				component:'set/base/index'
			},
			{
				meta:{title:'物流设置'},
				component:'set/express/index'
			},
			{
				meta:{title:'管理员管理'},
				component:'set/manager/index'
			},
			{
				meta:{title:'交易设置'},
				component:'set/payment/index'
			},
			{
				meta:{title:'404错误'},
				component:'error/404'
			},
		]
	},
	{
		meta:{title:'登录页'},
		component:'login/index'
	},
	{
		path:'*',
		redirect:{name:'index'},
	}
]

// 获取路由信息方法
let getRoutes = function(){
	// 自动生成路由
	createRoute(routes)
	return routes
}

// 自动生成路由
function createRoute(arr){
	for (let i = 0; i < arr.length; i++) {
		if (!arr[i].component) return
		// 去除index
		let val = getValue(arr[i].component)
		// 生成name
		arr[i].name = arr[i].name || val.replace(/\//g,'_')
		// 生成path
		arr[i].path = arr[i].path || `/${val}`
		// 自动生成component
		let componentFun = import(`../../views/${arr[i].component}.vue`)
		arr[i].component = ()=>componentFun
		if (arr[i].children && arr[i].children.length > 0) {
			createRoute(arr[i].children)
		}
	}
}

// 去除index
function getValue(str) {
	// str = login/index
	// 获取最后一个/的索引
	let index = str.lastIndexOf('/')
	// 获取最后一个/后面的值
	let val = str.substring(index+1,str.length)
	// 判断是不是index结尾
	if (val === 'index') {
		return str.substring(index,-1)
	}
	return str
}

export default getRoutes()