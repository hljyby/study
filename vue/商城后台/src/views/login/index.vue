<template>
	<div>
		
		<div class="container">
			<div class="row">
				<div class="col-12 col-sm-9 col-md-7 col-lg-5 m-auto pt-5">
					<div class="card mt-5">
						<div class="card-header bg-white">
							<h3 class="text-center mb-0 text-secondary">
								 {{$conf.logo}}
							</h3>
						</div>
						<div class="card-body">
							<el-form ref="ruleForm" :rules="rules" 
							:model="form">
								<el-form-item prop="username">
									<el-input v-model="form.username" 
									size="medium"
									placeholder="请输入用户名">
									</el-input>
								</el-form-item>
								<el-form-item prop="password">
									<el-input v-model="form.password" 
									size="medium" type="password"
									placeholder="请输入密码">
									</el-input>
								</el-form-item>
								<el-form-item>
									<el-button type="primary" size="medium"
									class="w-100" @click="submit"
									:loading="loading">
										{{loading? '登录中...' : '立即登录'}}
									</el-button>
								</el-form-item>
							</el-form>
						</div>
					</div>
				</div>
			</div>
		</div>
		
		
	</div>
</template>

<script>
	let ms = []
	import { mapGetters } from 'vuex'
	export default {
		data() {
			return {
				loading:false,
				form:{
					username:"",
					password:""
				},
				rules:{
					username:[
						{ required:true,message:"请输入用户名",trigger:'blur' }
					],
					password:[
						{ required:true,message:"请输入密码",trigger:'blur' }
					]
				}
			}
		},
		computed: {
			...mapGetters([
				'adminIndex'
			])
		},
		methods: {
			submit() {
				this.$refs.ruleForm.validate((e)=>{
					if (!e) return;
					// 提交表单
					this.loading = true
					this.axios.post('/admin/login',this.form).then(res=>{
						// 存储到vuex
						let data = res.data.data
						// 存储到本地存储
						this.$store.commit('login',data)
						// 存储权限规则
						if(data.role && data.role.rules){
							window.sessionStorage.setItem('rules',JSON.stringify(data.role.rules))
						}
						// 生成后台菜单
						this.$store.commit('createNavBar',data.tree)
						// 成功提示
						this.$message('登录成功')
						this.loading = false
						// 跳转后台首页
						this.$router.push({name:this.adminIndex})
					}).catch(err=>{
						this.loading = false
					})
				})
			}
		},
	}
</script>

<style>
</style>
