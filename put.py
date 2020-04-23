import sys
import paramiko
from os.path import split


def ssh_server_put(ip_or_hostname: str, username: str, password: str, address: str,
                   remote_address: str) -> None:
    transport = paramiko.Transport((ip_or_hostname, 22))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    if remote_address is None:
        try:
            sftp.put(address, "/home/" + username + "/Desktop/" + split(address)[-1])
        except Exception as e:
            print("无法连接远程服务端，请检查输入:")
            sys.exit(-1)

    else:
        try:
            sftp.put(address, remote_address + split(address)[-1])
        except Exception as e:
            print("无法连接远程服务端，请检查输入:")
            sys.exit(-1)
    sftp.close()
