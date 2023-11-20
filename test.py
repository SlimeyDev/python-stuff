import socket
import psutil

def get_network_info():
    hostname = socket.gethostname()
    ip_addresses = [ip for ip in socket.gethostbyname_ex(hostname)[2]]
    network_interfaces = psutil.net_if_addrs()

    network_info = f"Hostname: {hostname}\n"
    network_info += "IP Addresses:\n"
    for ip in ip_addresses:
        network_info += f"{ip}\n"
    network_info += "\nNetwork Interfaces:\n"
    for interface, addrs in network_interfaces.items():
        network_info += f"{interface}:\n"
        for addr in addrs:
            network_info += f"{addr.family.name} - {addr.address}\n"

    return network_info

# Example usage:
network_specs = get_network_info()
print(network_specs)