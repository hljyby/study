

server {
	listen 80;

	root /home/yby/data/www/django_rest_framework;

	index index.html index.htm index.nginx-debian.html;

	server_name www.ybybbb.com;

	location / {
		# 转发端口必须和uwsgi.ini中的socket端口一致
		uwsgi_pass  0.0.0.0:8000;
		include uwsgi_params;
		uwsgi_param UWSGI_SCRIPT django_rest_framework.wsgi;
		# 项目的根目录
		uwsgi_param UWSGI_CHDIR /home/yby/data/www/django_rest_framework;
	}
	
	location /static {

		alias /home/yby/data/www/django_rest_framework/static;

	}
}
 