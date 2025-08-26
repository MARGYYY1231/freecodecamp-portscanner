import socket
import ipaddress
import re
from common_ports import ports_and_services


def isVerbrose(open_ports, ip, hostname):
    if hostname is None:
        result = f"Open ports for {ip}\n"
    else:
        result = f"Open ports for {hostname} ({ip})\n"
    result += "PORT     SERVICE\n"
    for port in open_ports:
        service = ports_and_services.get(port, "unknown")
        result += f"{port:<9}{service}\n"

    return result.strip()


def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    ip = None
    hostname = None

    if re.search(r'[a-zA-Z]', target):
        try:
            ip = socket.gethostbyname(target)
            hostname = target
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

    if verbose:
        return isVerbrose(open_ports, ip, hostname)

    return (open_ports)
