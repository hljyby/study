<template>
	<div class="bg-white px-3 goods_create" style="margin: -20px;margin-top: -1rem;margin-bottom: 0!important;">
		<router-link :to="{name:'shop_goods_list'}" style="position: absolute;top: 12px;left: 200px;">
			<el-button size="mini">回到商品列表</el-button>
		</router-link>
		
		<div class="d-flex flex-wrap">
			
			<div style="width: 150px;height: 150px;cursor: pointer;position: relative;" class="border rounded d-flex align-items-center justify-content-center mr-3 mb-3" @click="chooseImage(index)" v-for="(item,index) in banners" :key="index">
				<img v-if="item.url" :src="item.url" 
				style="width: 100%;height: 100%;"/>
				<i v-else class="el-icon-plus text-muted" 
				style="font-size: 30px;"></i>
				
				<i class="el-icon-delete p-2 text-white"
				style="position: absolute;top: 0;right: 0;background-color: rgba(0,0,0,0.4);" @click.stop="deleteImage(index)"></i>
			</div>
			
			<div v-if="banners.length < 9" style="width: 150px;height: 150px;cursor: pointer;" class="border rounded d-flex align-items-center justify-content-center mr-3 mb-3" @click="chooseImage(-1)">
				<i class="el-icon-plus text-muted" 
				style="font-size: 30px;"></i>
			</div>
			
		</div>
		
		
		<el-button type="primary" style="position: fixed;bottom: 50px;right: 50px;" @click="submit">提交</el-button>
		
	</div>
</template>

<script>
	export default {
		inject:['app','layout'],
		data() {
			return {
				banners:[],
				id:0
			}
		},
		created() {
			this.id = this.$route.params.id
			if (!this.id) {
				this.$message({
					type:"error",
					message:"非法参数"
				})
				return this.$router.push({
					name:"shop_goods_list"
				})
			}
			// 获取之前的商品详情
			this.layout.showLoading()
			this.axios.get('/admin/goods/read/'+this.id,{
				token:true
			}).then(res=>{
				let data = res.data.data
				this.banners = data.goodsBanner
				this.layout.hideLoading()
			}).catch(err=>{
				this.layout.hideLoading()
			})
		},
		methods: {
			// 选择图片
			chooseImage(index){
				const MAX = 9
				let count = MAX - this.banners.length
				this.app.chooseImage((res)=>{
					let list = []
					if (index === -1) {
						list = [...this.banners,...res]
					} else {
						list = [...this.banners]
						list[index] = res[0]
					}
					this.banners = list
				},index === -1 ? count : 1)
			},
			// 删除大图
			deleteImage(index){
				this.$confirm('是否要删除该图片?', '提示', {
					confirmButtonText: '删除',
					cancelButtonText: '取消',
					type: 'warning'
				}).then(() => {
					this.banners.splice(index,1)
				})
			},
			submit(){
				this.layout.showLoading()
				this.axios.post('/admin/goods/banners/'+this.id,{
					banners:this.banners.map(item=>item.url)
				},{
					token:true
				}).then(res=>{
					this.$message({
						type:"success",
						message:"修改成功"
					})
					this.$router.push({
						name:"shop_goods_list"
					})
					this.layout.hideLoading()
				}).catch(err=>{
					this.layout.hideLoading()
				})
			}
		},
	}
</script>

<style>
	.goods_create .el-form-item{
		margin-bottom: 15px;
	}
</style>
