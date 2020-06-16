<template>
	<el-dialog title="商品规格选择" :visible.sync="createModel" width="80%" top="5vh">
		
		<el-container style="position: relative;height: 70vh;margin: -30px -20px;">
		  <el-container>
			<el-aside width="200px" style="position: absolute;top: 0;left: 0;bottom: 50px;" class="bg-white border-right">
				<!-- 侧边 | 规格卡片标题-->
				<ul class="list-group list-group-flush">
					<li class="list-group-item list-group-item-action"
					v-for="(item,index) in skusList" :key="index"
					:class="skuIndex === index ? 'sum-active':''"
					@click="changeSku(index)">{{item.name}}</li>
				</ul>
				
			</el-aside>
			<el-footer style="position: absolute;left: 0;bottom: 0;height: 50px;width: 200px;display: flex; align-items: center;justify-content: center;"
			class="border">
				<el-pagination
				  :current-page="page.current"
				  :page-sizes="page.sizes"
				  :page-size="page.size"
				  layout="prev, next"
				  :total="page.total"
				  @size-change="handleSizeChange"
				  @current-change="handleCurrentChange">
				</el-pagination>
			</el-footer>
			<el-container>
			  <el-header style="position: absolute;top: 0;left: 200px;right: 0;height: 60px;line-height: 60px;" class="border-top border-bottom">
					<el-button type="primary" size="mini" @click="doChooseAll">
						{{isChooseAll ? '取消全选' : '全选'}}
					</el-button>
			  </el-header>
			  <el-main style="position: absolute;top: 60px;left:200px;bottom: 0;right: 0;">
				  <div class="d-flex flex-wrap">
					  
					  <span class="border rounded py-1 px-2 m-2"
					  style="cursor: pointer;" v-for="(item,index) in skuItems"
					  :key="index" :class="item.ischeck ? 'sum-active':''"
					  @click="choose(item)">
						 {{item.name}}
					  </span>
					  
				  </div>
				 
			  </el-main>
			</el-container>
		  </el-container>
		</el-container>
		
		
		
		<div slot="footer" class="dialog-footer">
			<el-button @click="hide">取 消</el-button>
			<el-button type="primary" @click="confirm">确 定</el-button>
		</div>
	</el-dialog>
</template>

<script>
	import common from '@/common/mixins/common.js';
	export default {
		mixins:[common],
		data() {
			return {
				preUrl:"skus",
				loading:false,
				
				createModel:false,
				callback:false,
				// 选中的数组
				chooseList:[],
				// 数据
				skuIndex:0,
				skusList:[],
			}
		},
		computed: {
			// 当前规格下的规格属性列表
			skuItems() {
				let item = this.skusList[this.skuIndex]
				return item ? item.list : []
			},
			// 是否全选
			isChooseAll(){
				return this.skuItems.length === this.chooseList.length
			}
		},
		methods: {
			getListResult(e){
				console.log(e.list);
				this.skusList = e.list.map(item=>{
					let list = item.default.split(',')
					item.list = list.map(name=>{
						return {
							name:name,
							image:"",
							color:"",
							ischeck:false
						}
					})
					return item
				})
			},
			// 打开弹出层
			chooseSkus(callback){
				this.callback = callback
				this.createModel = true
			},
			// 确定
			confirm(){
				// 选中的skus
				if (typeof this.callback === 'function') {
					let item = this.skusList[this.skuIndex]
					this.callback({
						id:item.id,
						name:item.name,
						type:item.type,
						list:this.chooseList
					})
				}
				// 隐藏
				this.hide()
			},
			// 关闭弹出层
			hide(){
				this.unChooseAll()
				this.createModel = false
				this.callback = false
			},
			// 切换规格卡片
			changeSku(index){
				this.unChooseAll()
				this.skuIndex = index
			},
			// 选中规格属性
			choose(item){
				// 之前没有选中
				if (!item.ischeck) {
					// 加入选中列表
					this.chooseList.push(item)
					// 修改选中状态
					return item.ischeck = true
				}
				// 之前选中
				// 找到当前对象在chooseList中的索引
				let index = this.chooseList.findIndex(v=>{
					return v.id === item.id
				})
				// 找不到
				if (index < 0) return;
				// 从选中列表中移除
				this.chooseList.splice(index,1)
				// 修改选中状态
				item.ischeck = false
			},
			// 选中/取消选中
			doChooseAll(){
				let list = this.skusList[this.skuIndex].list
				// 已经全选
				if (this.isChooseAll) { // 取消全选
					return this.unChooseAll()
				}
				// 全选
				this.chooseList = list.map(v=>{
					// 设置全选状态
					v.ischeck = true
					return v
				})
			},
			// 取消选中所有
			unChooseAll(){
				let list = this.skusList[this.skuIndex].list
				// 取消选中状态
				list.forEach(v=>{
					v.ischeck = false
				})
				// 清空选中列表
				return this.chooseList = []
			}
		},
	}
</script>

<style>
	.sum-active{
		background-color: teal;
		color: #FFFFFF;
	}
</style>
