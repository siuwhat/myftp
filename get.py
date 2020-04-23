import paramiko
from os.path import split
import sys


def ssh_server_get(ip_or_hostname: str, username: str, password: str, address: str,
                   remote_address: str) -> None:
    transport = paramiko.Transport((ip_or_hostname, 22))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    # sftp.put("1.txt","/home/siuwhat/Desktop/1.txt")
    if address is None:
        try:
            sftp.get(remote_address, split(remote_address)[-1])
        except Exception as e:
            print("无法连接远程服务端，请检查输入:")
            sys.exit(-1)
    else:
        try:
            sftp.get(remote_address, address + split(remote_address)[-1])
        except Exception as e:
            print("无法连接远程服务端，请检查输入:")
            sys.exit(-1)
    sftp.close()
