from wsgiref.simple_server import make_server
import wsgiref, json


def load_file(file_name, **kwargs):
    try:
        with open('pages/' + file_name, 'r', encoding='utf8') as file:
            content = file.read()
            if kwargs:
                print('kwargs:', kwargs)
                # print('**kwargs:', **kwargs)
                content = content.format(**kwargs)
            return content
    except FileNotFoundError:
        print('未找到文件')
# *[1,2] = 1,2
#  **{a:1,b:2} == a=1,b=2 ,视为解构赋值

def demo_app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8')])

    print(environ['PATH_INFO'])
    print(environ['QUERY_STRING'])  # 获取GET请求传递的参数
    # 返回一个文件 可以file = open('xxx.txt','r',encoding='utf8') file.read(),html 文件也可以
    return ['hellow'.encode('utf8')]


if __name__ == '__main__':
    data = load_file('index.txt', names='正则', render='你猜')
    print(data)
    httpd = make_server('', 8000, demo_app)

    sa = httpd.socket.getsockname()

    print('Server Http on', sa[0], 'port', sa[1])
    import webbrowser

    webbrowser.open('http://localhost:8000/xyz?abc')
    # httpd.handle_request()  # 只处理一次请求
    httpd.serve_forever()  # 无限循环处理请求
