import socket
import ipaddress
import re
from common_ports import ports_and_services


def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    ip = None

    if re.search(r'[a-zA-Z]', target):
        try:
            ip = socket.gethostbyname(target)
        except socket.gaierror:
            return "Error: Invalid hostname"
    else:
        try:
            socket.inet_aton(target)
            ip = target
        except socket.error:
            return "Error: Invalid IP address"

    for port in range(port_range[0], port_range[1] + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if (s.connect_ex((ip, port)) == 0):
            open_ports.append(port)
        s.close()

    return (open_ports)
