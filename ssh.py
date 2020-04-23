import time
from get import ssh_server_get
from put import ssh_server_put

ip_or_hostname = input("$ 请输入目标服务端的ip或主机名:\n$ ")
print("请检查服务器端口22是否打开")
# TODO 提示
# 用命令行模块给参数
time.sleep(2)
username = input("$ 请输入用户名:\n$ ")
time.sleep(2)
password = input("$ 请输入登录密码:\n$ ")
time.sleep(2)
action = input("$ 请选择执行的操作:g/p:\n$ ")
while (not (action == "g")) and (not (action == "p")):
    action = input("$ 输入错误，请重新输入:g/p\n$ ")
time.sleep(2)
print("您的操作是:%s  " % action)
# 若未输入则默认地址
# 用命令行模块给参数
if action == "g":
    remote_address = input("$ 输入需要从目标服务端获得的文件的地址:\n$ ")
    address = input("$ 输入获得的文件存放地址:\n$ ")
    print("正在执行操作-- %s  " % action)
    ssh_server_get(ip_or_hostname, username, password, address, remote_address)
elif action == "p":
    address = input("$ 输入需要传输的文件地址:\n$ ")
    remote_address = input("$ 输入目标服务端存放文件的地址:\n$ ")
    print("正在执行操作-- %s  " % action)
    ssh_server_put(ip_or_hostname, username, password, address, remote_address)

time.sleep(2)
print("操作完成")
