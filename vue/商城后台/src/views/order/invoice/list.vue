<template>
	<div class="bg-white px-3" style="margin: -20px;margin-top: -1rem;margin-bottom: 0!important;">
		<button-search class="pt-3">
			<template #right>
				<div class="d-flex align-items-center">
					<el-date-picker size="medium"
					  v-model="search.time"
					  type="daterange"
					  range-separator="至"
					  start-placeholder="开始日期"
					  end-placeholder="结束日期">
					</el-date-picker>
					<el-input v-model="search.keyword" size="medium" placeholder="请输入订单号" style="width: 200px;" class="mx-2"></el-input>
					<el-button type="info" size="medium">搜索</el-button>
				</div>
			</template>
		</button-search>
	
	
		<el-table border class="mt-3"
		  :data="tableData"
		  style="width: 100%"
		   @selection-change="handleSelectionChange">
		  <el-table-column
			type="selection"
			width="45"
			align="center">
		  </el-table-column>
		  
		  <el-table-column
			label="订单编号"
			prop="name">
		  </el-table-column>
		 
		  <el-table-column
			align="center"
			prop="username"
			label="用户名">
		  </el-table-column>
		  
		  <el-table-column
			align="center"
			prop="price"
			label="开票金额">
		  </el-table-column>
		  
		  <el-table-column
			align="center"
			prop="price"
			label="抬头">
		  </el-table-column>
		  
		  <el-table-column
			align="center"
			prop="content"
			label="发票内容">
		  </el-table-column>
		  
		  <el-table-column
			align="center"
			prop="code"
			label="纳税人识别号">
		  </el-table-column>
		  
		  <el-table-column
			align="center"
			prop="create_time"
			label="创建时间">
		  </el-table-column>
		  
		  <el-table-column
			align="center"
			label="操作"
			width="150">
			<template slot-scope="scope">
				<el-button-group>
				  <el-button type="danger" size="mini" 
				  plain @click="deleteItem(scope)"
				  >删除</el-button>
				</el-button-group>
			</template>
		  </el-table-column>
		</el-table>
		<div style="height: 60px;"></div>
		<el-footer class="border-top d-flex align-items-center px-0 position-fixed bg-white" style="bottom: 0;left: 200px;right: 0;z-index: 100;">
		  <div style="flex: 1;" class="px-2">
			  <el-pagination
			  :current-page="currentPage"
			  :page-sizes="[100, 200, 300, 400]"
			  :page-size="100"
			  layout="total, sizes, prev, pager, next, jumper"
			  :total="400">
			</el-pagination>
		  </div>
		</el-footer>
	</div>
</template>

<script>
	import buttonSearch from "@/components/common/button-search.vue"
	export default {
		components: {
			buttonSearch
		},
		data() {
			return {
				tableData: [],
				currentPage:1,
				multipleSelection: [],
				
				search:{
					time:"",
					keyword:""
				}
			}
		},
		created() {

		},
		methods: {
			// 选中
			handleSelectionChange(val) {
				this.multipleSelection = val;
			},
			// 删除单个
			deleteItem(scope){
				this.$confirm('是否要删除该规格?', '提示', {
					confirmButtonText: '删除',
					cancelButtonText: '取消',
					type: 'warning'
				}).then(() => {
					this.tableData.splice(scope.$index,1)
					this.$message({
						message: '删除成功',
						type: 'success'
					});
				})
			}
		},
	}
</script>

<style>
.sku-list-item>i{
	display: none;
	cursor: pointer;
}
.sku-list-item:hover{
	background-color: #f4f4f4;
}
.sku-list-item:hover>font{
	display: none;
}
.sku-list-item:hover>i{
	display: inline-block;
}
</style>
