
import os
from ftplib import FTP
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading


def ftpConnect(ftpserver, port):
    # FTP.encoding = 'utf8'
    ftp = FTP()
    encoding = "utf8"  # 默认编码
    ftp.encoding = encoding
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
    ftppath = os.path.join(ftpPath, ftpfile)
    thread_name = threading.current_thread().name
    # print(path, thread_name)
    if os.path.exists(path):
        return ftp
    with open(path, 'wb') as fid:
        print('正在下载：', ftpfile, thread_name)
        # ftp.cwd(ftpPath)
        ftp.retrbinary('RETR {0}'.format(ftppath),
                       fid.write, bufsize)  # 接收服务器文件并写入本地文件
        print('下载完毕。', ftpfile, thread_name)
    return ftp
  # 退出ftp连接


def ftpDisConnect(ftp):
    ftp.result().quit()


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=3)
    # 输入参数
    ftpserver = '192.168.0.109'
    ftpath = '/Download/闪电下载/【重磅推荐】知名Twitter户外露出网红FSS冯珊珊和妹子一起挑战全裸便利店购物 小老板看了一脸懵/'
    localpath = 'F:/闪电下载/【重磅推荐】知名Twitter户外露出网红FSS冯珊珊和妹子一起挑战全裸便利店购物 小老板看了一脸懵/'
    port = 3721
    ftp = ftpConnect(ftpserver, port)
    ftp.cwd(ftpath)
    filenameList = ftp.nlst()
    if not os.path.exists(localpath):
        os.makedirs(localpath)
    for i in filenameList:
        ftps = ftpConnect(ftpserver, port)
        executor.submit(ftpDownloadFile, ftp=ftps, ftpfile=i,
                        localfile=localpath, ftpPath=ftpath).add_done_callback(ftpDisConnect)
    executor.shutdown(True)
    ftp.quit()
    print("\n+-------- OK!!! --------+\n")
