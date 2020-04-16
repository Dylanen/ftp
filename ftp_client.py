"""
ftp 客户端
c/s模式   发送请求 获取结果
"""

from socket import *

ADDR = ('127.0.0.1',8800)

class FTPClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L') # 发送请求
        # 等待回复 YES NO
        data = self.sockfd.recv(128).decode()
        if data == "YES":
            # 接收文件列表
            data = self.sockfd.recv(4096)
            print(data.decode())
        else:
            print("获取文件列表失败")



# 链接服务端
def main():
    s = socket()
    s.connect(ADDR)

    # 实例化对象
    ftp = FTPClient(s)

    while True:
        print("================命令选项==================")
        print("=======          list                ===")
        print("=======         get file             ===")
        print("=======         put file             ===")
        print("=======          quit                ===")
        print("=========================================")

        cmd = input("请输入命令:")
        if cmd == "list":
            ftp.do_list()



if __name__ == '__main__':
    main()