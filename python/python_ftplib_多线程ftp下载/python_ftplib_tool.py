import os
from ftplib import FTP
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading

ftpServer = '192.168.0.109'  # 服务器地址
ftpPath = '/Download/闪电下载/2/'  # ftp路径
localPath = 'F:/闪电下载/2/'  # 保存的路径
ftpPort = 3721  # 端口号
username = "yby"  # 用户名密码 没有制空
password = "970829"

# 上面这些参数可以写在文件里在通过
# with open(path,r,"utf8") as f:
#   f.readLine()
# 多线程FTP下载


class MyFTP(FTP):
    encoding = "utf8"  # 默认编码

    def getSubdir(self, *args):
        '''拷贝了 nlst() 和 dir() 代码修改，返回详细信息而不打印'''
        cmd = 'LIST'
        func = None
        if args[-1:] and type(args[-1]) != type(''):
            args, func = args[:-1], args[-1]
        for arg in args:
            cmd = cmd + (' ' + arg)
        files = []
        self.retrlines(cmd, files.append)
        return files
    # 自定义函数获取 目录下的树形菜单

    def getdirs(self, ftpPath="/Download/", rootPath='F:/phone/'):
        """返回目录列表，包括文件简要信息"""

        """
            @ des: 获取dirPath路径下的所有文件和文件夹的树形结构
            @ params:dirPath ftp服务器上的，你想要下载的文件夹
            @ params:rootPath 你想要保存的本地根路径

        """
        self.cwd(ftpPath)
        files = self.getSubdir()
        fileList = []
        dirList = []
        for item in files:
            filetype = item.split(" ")[0][0]  # 处理返回结果，仅需要目录标识：d标识目录 - 标识文件
            y = list(filter(lambda s: s and s.strip(), item.split(" ")))
            filename = " ".join(y[8:])  # 获取文件名 注意文件名内不能有冒号

            if filename != "." and filename != "..":  # 去除. ..
                if filetype == 'd':  # 文件夹

                    dir = self.getdirs(
                        os.path.join(ftpPath, filename) + "/",
                        os.path.join(rootPath, filename) + "/"
                    )
                    dirList.append(dir)
                elif filetype == '-':  # 文件
                    fileList.append(filename)

        fileSet = {   # 当前
            "currentPath": ftpPath,
            'fileList': fileList,
            'subDir': dirList,
            "localPath": rootPath
        }
        return fileSet

    # 连接ftp服务器
    def ftpConnect(self, ftpserver, port):
        # FTP.encoding = 'utf8'
        try:
            self.connect(ftpserver, port)
            self.login(username, password)
        except:
            raise IOError('\n FTP connection failed, please check the code!')
        else:
            print(self.getwelcome())  # 打印登陆成功后的欢迎信息
            print('\n+------- ftp connection successful!!! --------+')

    # 下载单个文件
    def ftpDownloadFile(self, fileName, localPath, ftpPath):

        bufsize = 8192  # 缓冲区大小 这个应该是默认的
        localFull = os.path.join(localPath, fileName)
        ftpFull = os.path.join(ftpPath, fileName)

        thread_name = threading.current_thread().name

        if os.path.exists(localFull):
            return "该文件已存在"
        with open(localFull, 'wb') as fid:
            print('正在下载：', fileName, "线程名：", thread_name)

            self.retrbinary(
                'RETR {0}'.format(ftpFull),
                fid.write,
                bufsize
            )
            # 接收服务器文件并写入本地文件
            print("下载完毕。线程名：", thread_name)
        return

    # 中间件 进程池不能阻挡for循环的脚步，只能放到队列里等待执行，所以做一个中间件缓冲一下，目的是执行到那个进程就新建一个连接
    def midDownload(self, fileName, localPath, ftpPath):
        innerFTP = MyFTP()
        innerFTP.ftpConnect(ftpServer, ftpPort)
        innerFTP.ftpDownloadFile(fileName, localPath, ftpPath)
        innerFTP.quit()

    # 批量下载
    def downLoad(self, fileSet, localPath):

        if not os.path.exists(localPath):
            os.makedirs(localPath)

        if not localPath[-1] == "/":
            localPath = localPath + "/"

        for dir in fileSet:
            ftpPath = dir.get('currentPath')
            self.downLoad(dir.get("subDir"), dir.get("localPath"))

            for fileName in dir.get('fileList'):
                # self.ftpDownloadFile(
                #     fileName=fileName,
                #     localPath=dir.get("localPath"),
                #     ftpPath=ftpPath
                # )
                self.pool.submit(
                    self.midDownload,
                    fileName=fileName,
                    localPath=dir.get("localPath"),
                    ftpPath=ftpPath
                )

    # 下载整个目录下的文件

    def ftpDownload(self, ftpPath, localPath):
        '''
        :param ftpPath: ftp中的目标路径
        :param localPath: 存放下载文件的本地路径
        :return:
        '''
        print('Remote Path: {0}'.format(ftpPath))
        self.cwd(ftpPath)
        if not localPath[-1] == "/":
            localPath = localPath + "/"

        if not ftpPath[-1] == "/":
            ftpPath = ftpPath + "/"

        print('成功进入ftp服务器：', ftpPath)
        fileSet = self.getdirs(ftpPath=ftpPath, rootPath=localPath)
        fileSet = [fileSet]
        self.downLoad(fileSet, localPath)
        return True

    def createThreadPool(self, size):
        self.pool = ThreadPoolExecutor(max_workers=size)


# 程序入口
if __name__ == '__main__':
    # 输入参数
    downloadFTP = MyFTP()
    downloadFTP.createThreadPool(5)
    downloadFTP.ftpConnect(ftpServer, ftpPort)
    downloadFTP.ftpDownload(ftpPath, localPath)
    downloadFTP.pool.shutdown(True)
    downloadFTP.quit()
    print("\n+-------- OK!!! --------+\n")
