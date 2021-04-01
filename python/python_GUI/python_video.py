import re
import tkinter as tk

from urllib import parse
# 消息盒子
import tkinter.messagebox as ms
# 控制浏览器
import webbrowser


class App:
    def __init__(self, width=500, height=500):
        self.w = width
        self.h = height

        self.title = "视频解析助手"

        self.root = tk.Tk(className=self.title)

        self.url = tk.StringVar()

        self.v = tk.IntVar()
        self.v.set(1)

        # 软件空间划分

        frame_1 = tk.Frame(self.root)

        frame_2 = tk.Frame(self.root)

        group = tk.Label(frame_1, text="播放通道：", padx=10, pady=10)

        tb = tk.Radiobutton(frame_1, text="唯一通道",
                            variable=self.v, value=1, width=10, height=3)

        label = tk.Label(frame_2, text="请输入视频地址：")

        entry = tk.Entry(frame_2, textvariable=self.url,
                         highlightcolor='Fuchsia', highlightthickness=1, width=30)

        play = tk.Button(frame_2, text="播放", font=(
            '楷体', 12), fg="Purple", width=2, height=1,command=self.video_play)

        # 激活空间
        frame_1.pack()
        frame_2.pack()
        # 位置确定
        group.grid(row=0,column=0)
        tb.grid(row=0,column=1)
        # 空间与空间之间是独立的
        label.grid(row=0,column=0)
        entry.grid(row=0,column=1)
        play.grid(row=0,column=2,padx=10,ipadx=5)




    def loop(self):
        self.root.mainloop()

    def video_play(self):
        # 视频解析网站地址
        port = 'http://www.wmxz.wang/video.php?url='
        # port = 'http://www.vipjiexi.com/vip.php?url='

        # 正则表达式判定是否为合法连接
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):
            # 拿到用户输入的视频网址
            ip = self.url.get()

            # 视频连接加密
            ip = parse.quote_plus(ip)

            # 用浏览器打开网址
            webbrowser.open(port + ip)

        else:
            ms.showerror(title='错误', message='视频链接地址无效，请重新输入！')


if __name__ == "__main__":
    app = App()
    app.loop()