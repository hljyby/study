<template>
	<div class="bg-white px-3" style="margin: -20px;margin-top: -1rem;margin-bottom: 0!important;">
		<button-search ref="buttonSearch" class="pt-3" placeholder="要搜索的商品名称" @search="searchEvent" :showSuperSearch="false"></button-search>
	
	
		<el-table border class="mt-3"
		  :data="tableData"
		  style="width: 100%"
		  >
		  
		  <el-table-column type="expand">
			<template slot-scope="scope">
			  <div class="media">
			    <img class="mr-3" :src="scope.row.user.avatar" alt="Generic placeholder image" style="height: 70px;width: 70px;border-radius: 100%;">
			    <div class="media-body">
			      <h6 class="mt-0 d-flex">
					  {{scope.row.user.username}} <small>{{scope.row.review_time}}</small>
					  <el-button v-if="!scope.row.extra && !textareaEdit" class="ml-auto" type="info" size="mini" @click="textareaEdit = true">回复</el-button>
				  </h6>
			      {{scope.row.review.data}}
				  <div class="py-2">
					  <img v-for="(item,index) in scope.row.review.image" :key="index" :src="item" style="max-width: 100px;max-height: 100px;"/>
				  </div>
				  
				  <div v-if="textareaEdit">
					  <el-input 
					    type="textarea"
					    :rows="2"
					    placeholder="请输入评价内容"
					    v-model="textarea">
					  </el-input>
					  <div class="py-2">
						  <el-button class="ml-auto mr-2" type="success" size="mini"
						  @click="review(scope.row.id)">回复</el-button>
						  <el-button class="ml-auto" type="info" size="mini" @click="closeTextarea">取消</el-button>
					  </div>
				  </div>
				  
				  <div v-if="scope.row.extra">
			      <div class="media mt-3 bg-light p-2 rounded" v-for="(item,index) in scope.row.extra"
				  :key="index">
			        <div class="media-body">
			          <h6 class="mt-0 d-flex">
						  客服
						  <el-button v-if="!textareaEdit" 
						  class="ml-auto" type="info" size="mini"
						  @click="openTextarea(item.data)">修改</el-button>
					  </h6>
					  {{item.data}}
			        </div>
			      </div>
				  </div>
			    </div>
			  </div>
			</template>
		  </el-table-column>
		  
		  <el-table-column
			label="ID"
			width="70"
			align="center"
			prop="id">
		  </el-table-column>
		  <el-table-column
			label="商品"
			width="380">
			<template slot-scope="scope">
				<div class="media">
				  <img class="mr-3" style="width: 60px;height: 60px;" 
				  :src="scope.row.goods_item.cover">
				  <div class="media-body">
					<p class="mt-0">{{scope.row.goods_item.title}}</p>
				  </div>
				</div>
			</template>
		  </el-table-column>
		  <el-table-column
			width="250"
			label="评价信息">
			<template slot-scope="scope">
				<div class="d-flex flex-column">
					<p>用户名：{{scope.row.user.username}}</p>
					<p>评分：<el-rate
						  v-model="scope.row.rating"
						  disabled
						  show-score
						  text-color="#ff9900"
						  score-template="{value}">
						</el-rate></p>
				</div>
			</template>
		  </el-table-column>
		  <el-table-column
			prop="review_time"
			align="center"
			label="评价时间">
		  </el-table-column>
		  <el-table-column
			align="center"
			label="是否显示"
			width="150">
			<template slot-scope="scope">
				<el-button
				:type="scope.row.status ? 'success' : 'danger'" 
				size="mini"
				@click="changeStatus(scope.row)"
				plain>{{scope.row.status ? '启用' : '禁用'}}
				</el-button>
			</template>
		  </el-table-column>
		</el-table>
		<div style="height: 60px;"></div>
		<el-footer class="border-top d-flex align-items-center px-0 position-fixed bg-white" style="bottom: 0;left: 200px;right: 0;z-index: 100;">
		  <div style="flex: 1;" class="px-2">
			  <el-pagination
			    :current-page="page.current"
			    :page-sizes="page.sizes"
			    :page-size="page.size"
			    layout="total, sizes, prev, pager, next, jumper"
			    :total="page.total"
			    @size-change="handleSizeChange"
			    @current-change="handleCurrentChange">
			  </el-pagination>
		  </div>
		</el-footer>

	</div>
</template>

<script>
	import buttonSearch from "@/components/common/button-search.vue"
	import common from '@/common/mixins/common.js';
	export default {
		inject:['layout'],
		mixins:[common],
		components: {
			buttonSearch
		},
		data() {
			return {
				preUrl:"goods_comment",
				
				
				textarea:"",
				textareaEdit:false,
				
				tableData:[],

				title:""
			}
		},
		methods: {
			openTextarea(data){
				this.textarea = data
				this.textareaEdit = true
			},
			review(id){
				if(this.textarea == ''){
					return this.$message({
						message: '回复内容不能为空',
						type: 'error'
					})
				}
				this.layout.showLoading()
				this.axios.post('/admin/goods_comment/review/'+id,{
					data:this.textarea
				},{
					token:true
				}).then(res=>{
					this.closeTextarea()
					this.$message({
						message: '回复成功',
						type: 'success'
					})
					this.getList()
					this.layout.hideLoading()
				}).catch(err=>{
					this.layout.hideLoading()
				})
			},
			closeTextarea(){
				this.textarea = ''
				this.textareaEdit = false
			},
			getListResult(e){
				console.log(e.list);
				this.tableData = e.list
			},
			// 获取请求列表分页url
			getListUrl(){
				return `/admin/${this.preUrl}/${this.page.current}?limit=${this.page.size}&title=${this.title}`
			},
			searchEvent(e){
				this.title = e
				this.getList()
			}
		},
	}
</script>

<style>
</style>
