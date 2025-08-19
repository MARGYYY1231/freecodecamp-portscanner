import socket

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

    try:
        try:
            ip = str(ipaddress.ip_address(target))
            hostname = target
        except ValueError:
            try:
                ip = str(ipaddress.ip_address(target))
                hostname = target
            except socket.gaierror:
                return "Error: Invalid hostname"
    except Exception:
        return "Error: Invalid IP address"

    
    for port in range(port_range[0], port_range[1] + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        s.close()

    if verbose:
        result = f"Open ports for {hostname} ({ip})\n"
        result += "PORT     SERVICE\n"
        for port in open_ports:
            service = ports_and_services.get(port, "unknown")
            result += f"{port:<8}{service}\n"
        return result.strip()
    else:
        return(open_ports)