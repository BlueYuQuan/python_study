# -*- coding: utf-8 -*-
import socket
 
def main():
    #1.创建套接字 
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #补充：绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
    local_addr = ('', 4414) #  ip地址和端口号，ip一般不用写，表示本机的任何一个ip
    s.bind(local_addr)

    #2.获取要发送的数据
    send_data = input('请输入要发送的内容能够')

    #3.要发送的目的地址('IP',端口)
    aim_addr = ('127.0.0.1',4415)

    #4.发送数据sendto(IP,端口)
    s.sendto(send_data.encode("utf-8"),aim_addr)

    #5.接受数据recvfrom(规定接受数据的大小),接受的端口号就是发出去的端口号，如果不中断这个程序，那么端口号是不变的
    receive_data = s.recvfrom(1024)

    #6.打印接受到的信息
    #print("接收到了："+(str)receive_data)
    print(receive_data[0].decode('utf-8')) # 打印具体发生的信息
    print(receive_data[1]) # 打印源IP和port

    # 关闭
    s.close()
 
 
if __name__ == "__main__":
    main()
#记得务必关闭防火墙，或者开放目标端口
