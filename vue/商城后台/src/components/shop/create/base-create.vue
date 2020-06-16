<template>
	<el-form ref="form" label-width="80px">
		<el-form-item label="商品名称">
			<el-input :value="title" 
			@input="vModel('title',$event)" 
			placeholder="请输入商品名称，不能超过60个字符" 
			class="w-50"></el-input>
		</el-form-item>
		<el-form-item label="商品分类">
			<el-cascader
			 :value="category"
			 @input="vModel('category',$event)" 
			 :options="options"></el-cascader>
		</el-form-item>
		<el-form-item label="商品描述">
			<el-input  type="textarea" :value="desc" 
			@input="vModel('desc',$event)"  placeholder="选填，商品卖点简述，例如：此款商品美观大方 性价比较高 不容错过" class="w-50"></el-input>
		</el-form-item>
		<el-form-item label="商品单位">
			<el-input :value="unit" 
			@input="vModel('unit',$event)"  placeholder="请输入商品单位" class="w-50"></el-input>
		</el-form-item>
		<el-form-item label="总库存">
			<el-input type="number" :value="stock" 
			@input="vModel('stock',$event)"  
			class="w-25">
				<template slot="append">件</template>
			</el-input>
		</el-form-item>
		<el-form-item label="库存预警">
			<el-input type="number" :value="min_stock" 
			@input="vModel('min_stock',$event)" class="w-25">
				<template slot="append">件</template>
			</el-input>
		</el-form-item>
		<el-form-item label="库存显示">
			<el-radio-group
			:value="display_stock"
			@input="vModel('display_stock',$event)" >
				<el-radio :label="1" border>是</el-radio>
				<el-radio :label="0" border>否</el-radio>
			</el-radio-group>
		</el-form-item>
		<el-form-item label="是否上架">
			<el-radio-group
			:value="status"
			@input="vModel('status',$event)" >
				<el-radio :label="0" border>放入仓库</el-radio>
				<el-radio :label="1" border>立即上架</el-radio>
			</el-radio-group>
		</el-form-item>
		<el-form-item label="运费模板">
			<el-select :value="express" 
			@input="vModel('express',$event)" 
			placeholder="请选择运费模板">
				<el-option label="区域一" 
				value="shanghai"></el-option>
				<el-option label="区域二" 
				value="beijing"></el-option>
			</el-select>
		</el-form-item>
	</el-form>
</template>

<script>
	import {mapState,mapMutations} from "vuex"
	export default {
		data() {
			return {
				tabIndex: 0,
				options: [{
					value: 'zhinan',
					label: '指南',
					children: [{
						value: 'shejiyuanze',
						label: '设计原则',
						children: [{
							value: 'yizhi',
							label: '一致'
						}, {
							value: 'fankui',
							label: '反馈'
						}, {
							value: 'xiaolv',
							label: '效率'
						}, {
							value: 'kekong',
							label: '可控'
						}]
					}, {
						value: 'daohang',
						label: '导航',
						children: [{
							value: 'cexiangdaohang',
							label: '侧向导航'
						}, {
							value: 'dingbudaohang',
							label: '顶部导航'
						}]
					}]
				}, {
					value: 'zujian',
					label: '组件',
					children: [{
						value: 'basic',
						label: 'Basic',
						children: [{
							value: 'layout',
							label: 'Layout 布局'
						}, {
							value: 'color',
							label: 'Color 色彩'
						}, {
							value: 'typography',
							label: 'Typography 字体'
						}, {
							value: 'icon',
							label: 'Icon 图标'
						}, {
							value: 'button',
							label: 'Button 按钮'
						}]
					}, {
						value: 'form',
						label: 'Form',
						children: [{
							value: 'radio',
							label: 'Radio 单选框'
						}, {
							value: 'checkbox',
							label: 'Checkbox 多选框'
						}, {
							value: 'input',
							label: 'Input 输入框'
						}, {
							value: 'input-number',
							label: 'InputNumber 计数器'
						}, {
							value: 'select',
							label: 'Select 选择器'
						}, {
							value: 'cascader',
							label: 'Cascader 级联选择器'
						}, {
							value: 'switch',
							label: 'Switch 开关'
						}, {
							value: 'slider',
							label: 'Slider 滑块'
						}, {
							value: 'time-picker',
							label: 'TimePicker 时间选择器'
						}, {
							value: 'date-picker',
							label: 'DatePicker 日期选择器'
						}, {
							value: 'datetime-picker',
							label: 'DateTimePicker 日期时间选择器'
						}, {
							value: 'upload',
							label: 'Upload 上传'
						}, {
							value: 'rate',
							label: 'Rate 评分'
						}, {
							value: 'form',
							label: 'Form 表单'
						}]
					}, {
						value: 'data',
						label: 'Data',
						children: [{
							value: 'table',
							label: 'Table 表格'
						}, {
							value: 'tag',
							label: 'Tag 标签'
						}, {
							value: 'progress',
							label: 'Progress 进度条'
						}, {
							value: 'tree',
							label: 'Tree 树形控件'
						}, {
							value: 'pagination',
							label: 'Pagination 分页'
						}, {
							value: 'badge',
							label: 'Badge 标记'
						}]
					}, {
						value: 'notice',
						label: 'Notice',
						children: [{
							value: 'alert',
							label: 'Alert 警告'
						}, {
							value: 'loading',
							label: 'Loading 加载'
						}, {
							value: 'message',
							label: 'Message 消息提示'
						}, {
							value: 'message-box',
							label: 'MessageBox 弹框'
						}, {
							value: 'notification',
							label: 'Notification 通知'
						}]
					}, {
						value: 'navigation',
						label: 'Navigation',
						children: [{
							value: 'menu',
							label: 'NavMenu 导航菜单'
						}, {
							value: 'tabs',
							label: 'Tabs 标签页'
						}, {
							value: 'breadcrumb',
							label: 'Breadcrumb 面包屑'
						}, {
							value: 'dropdown',
							label: 'Dropdown 下拉菜单'
						}, {
							value: 'steps',
							label: 'Steps 步骤条'
						}]
					}, {
						value: 'others',
						label: 'Others',
						children: [{
							value: 'dialog',
							label: 'Dialog 对话框'
						}, {
							value: 'tooltip',
							label: 'Tooltip 文字提示'
						}, {
							value: 'popover',
							label: 'Popover 弹出框'
						}, {
							value: 'card',
							label: 'Card 卡片'
						}, {
							value: 'carousel',
							label: 'Carousel 走马灯'
						}, {
							value: 'collapse',
							label: 'Collapse 折叠面板'
						}]
					}]
				}, {
					value: 'ziyuan',
					label: '资源',
					children: [{
						value: 'axure',
						label: 'Axure Components'
					}, {
						value: 'sketch',
						label: 'Sketch Templates'
					}, {
						value: 'jiaohu',
						label: '组件交互文档'
					}]
				}]
			}
		},
		computed: {
			...mapState({
				title: state=>state.goods_create.title,
				category: state=>state.goods_create.category,
				desc:state=>state.goods_create.desc,
				unit:state=>state.goods_create.unit,
				stock:state=>state.goods_create.stock,
				min_stock:state=>state.goods_create.min_stock,
				display_stock:state=>state.goods_create.display_stock,
				status:state=>state.goods_create.status,
				express:state=>state.goods_create.express,
			}),
			// 其他计算属性
		},
		methods: {
			...mapMutations(['vModelState']),
			// 修改表单的值
			vModel(key,value){
				this.vModelState({ key,value })
			},
		},
	}
</script>

<style>
</style>
