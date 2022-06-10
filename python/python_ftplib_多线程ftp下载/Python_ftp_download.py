import os
from ftplib import FTP


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

    def getdirs(self, dirname=None, rootPath='F:/phone/'):
        """返回目录列表，包括文件简要信息"""
        if dirname != None:
            ftp.cwd(dirname)
        files = self.getSubdir()
        currentPath = self.pwd()

        if not currentPath[-1] == "/":
            currentPath + "/"
        fileList = []
        dirList = []
        for item in files:
            filetype = item.split(" ")[0][0]  # 处理返回结果，仅需要目录标识：d标识目录 - 标识文件
            # filename = item.split(" ")[-1]    # 处理返回结果，仅需要目录名称或文件名称
            y = list(filter(lambda s: s and s.strip(), item.split(" ")))
            filename = " ".join(y[8:])

            if filename != "." and filename != "..":  # 去除. ..
                if filetype == 'd':

                    dir = self.getdirs(
                        filename, os.path.join(rootPath, filename) + "/")
                    dirList.append(dir)
                elif filetype == '-':

                    fileList.append(filename)
        if dirname != None:
            self.cwd("..")
        fileSet = {
            "currentPath": currentPath,
            'fileList': fileList,
            'subDir': dirList,
            "localPath": rootPath}
        return fileSet
# 连接ftp服务器


def ftpConnect(ftpserver, port):
    # FTP.encoding = 'utf8'
    ftp = MyFTP()
    try:
        ftp.connect(ftpserver, port)
        ftp.login('Administrator', "970829")
    except:
        raise IOError('\n FTP connection failed, please check the code!')
    else:
        print(ftp.getwelcome())  # 打印登陆成功后的欢迎信息
        print('\n+------- ftp connection successful!!! --------+')
        return ftp


# 下载单个文件
def ftpDownloadFile(ftp, ftpfile, localfile, ftpPath):
    bufsize = 8192

    path = os.path.join(localfile, ftpfile)
    if os.path.exists(path):
        return
    print(path)
    with open(path, 'wb') as fid:
        print('正在下载：', ftpfile)
        ftp.cwd(ftpPath)
        ftp.retrbinary('RETR {0}'.format(ftpfile),
                       fid.write, bufsize)  # 接收服务器文件并写入本地文件
        print('下载完毕。')

# 批量下载


def downLoad(ftp, fileSet, localpath):

    print("localpath", localpath)
    # print("fileSet", fileSet)
    if not os.path.exists(localpath):
        os.makedirs(localpath)

    if not localpath[-1] == "/":
        localpath = localpath + "/"

    for dir in fileSet:
        downLoad(ftp, dir.get("subDir"), dir.get("localPath"))
        ftpPath = dir.get('currentPath')
        for fileName in dir.get('fileList'):
            ftpDownloadFile(ftp, fileName, dir.get("localPath"), ftpPath)


# 下载整个目录下的文件


def ftpDownload(ftp, ftpath, localpath):
    '''
    :param ftp: 登陆ftp返回的信息
    :param ftpath: ftp中的目标路径
    :param localpath: 存放下载文件的本地路径
    :return:
    '''
    print('Remote Path: {0}'.format(ftpath))
    if not os.path.exists(localpath):
        os.makedirs(localpath)
    ftp.cwd(ftpath)
    print('成功进入ftp服务器：', ftpath)
    fileSet = ftp.getdirs(rootPath=localpath)
    fileSet["localPath"] = localpath
    print(fileSet)
    fileSet = [fileSet]
    downLoad(ftp, fileSet, localpath)
    return True
    # for file in ftp.nlst():
    #     print('file:', file)
    #     local = os.path.join(localpath, file)
    #     file_path = os.path.join(ftpath, file)
    #     if not os.path.exists(local):
    #         os.makedirs(local)
    #     ftp.cwd(file_path)
    #     print('进入子目录：--', file_path)
    #     for sub_file in ftp.nlst():
    #         ftpDownloadFile(ftp, sub_file, local)
    #     ftp.cwd('..')
    #     return True


# 退出ftp连接
def ftpDisConnect(ftp):
    ftp.quit()


# 程序入口
if __name__ == '__main__':
    # 输入参数
    ftpserver = '192.168.0.109'
    ftpath = '/UCDownloads/VideoData/'
    localpath = 'F:/phone/'
    port = 3721
    ftp = ftpConnect(ftpserver, port)
    flag = ftpDownload(ftp, ftpath, localpath)
    print(flag)

    # ftp.cwd(ftpath)
    # dirset = ftp.getdirs()
    # print(dirset)
    ftpDisConnect(ftp)
    print("\n+-------- OK!!! --------+\n")


# from ftplib import FTP            # 导入ftplib模块
# ftp=FTP()                         # 获取ftp变量
# ftp.set_debuglevel(2)             # 打开调试级别2，显示详细信息
# ftp.connect("host","port")          #连接的ftp sever服务器
# ftp.login("usrname","password")      # 用户登陆
# print(ftp.getwelcome())            # 打印欢迎信息
# ftp.cwd("xxx/xxx")                # 进入远程目录
# ftp.retrbinaly("RETR filename.txt",file_handle,bufsize) # 接收服务器上文件并写入本地文件
# ftp.set_debuglevel(0)             #关闭调试模式
# ftp.quit()                        #退出ftp

# ftp.cwd(ftppath)                 # 设置ftp当前操作的路径
# ftp.dir()                         # 显示目录下所有文件信息
# ftp.nlst()                        # 获取目录下的文件，返回一个list
# ftp.mkd(pathname)                 # 新建远程目录
# ftp.pwd()                         # 返回当前所在路径
# ftp.rmd(dirname)                  # 删除远程目录
# ftp.delete(filename)              # 删除远程文件
# ftp.rename(fromname, toname) # 将fromname修改名称为toname。
# ftp.storbinaly("STOR filename.txt",fid,bufsize)  # 上传目标文件
# ftp.retrbinary("RETR filename.txt",fid,bufsize)  # 下载FTP文件
