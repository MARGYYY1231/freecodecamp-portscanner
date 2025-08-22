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
            ip = str(ipaddress.ip_address(target))
        except socket.error:
            return "Error: Invalid IP address"

    return (open_ports)
