"""Черновой файл, который нужно будет разносить по ддд"""

import os

import netmiko
from dotenv import load_dotenv

load_dotenv()

class LinuxSSH:
    """Прямая работа с линуксом"""

    def __init__(self, ip, host, username, password, port):
        self.creds = {
            "ip": ip,
            "host": host,
            "username": username,
            "password": password,
            "device_type": "linux",
            "port": port
        }
        self.ssh_conect = netmiko.ConnectHandler(**self.creds)


    def send_command(self, command_string):
        return self.ssh_conect.send_command(command_string, read_timeout=10.0)


if __name__ == "__main__":
    linux_ssh = LinuxSSH(
        ip=os.getenv("IP_VDS"),
        host=os.getenv("HOSTNAME_VDS"),
        username=os.getenv("USERNAME_VDS"),
        password=os.getenv("PASS_VDS"),
        port=os.getenv("SSH_PORT_VDS")
    )
    command = "pwd"
    print(linux_ssh.send_command(command))

