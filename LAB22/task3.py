import ipaddress
import random
import time
SAMPLE_MAC_PREFIXES = ["00:11:22", "66:77:88", "AA:BB:CC", "DE:AD:BE", "12:34:56"]
def simulate_device(ip):
    prefix = random.choice(SAMPLE_MAC_PREFIXES)
    suffix = ":".join(f"{random.randint(0,255):02x}" for _ in range(3))
    mac = prefix + ":" + suffix
    # Optional: fake hostname
    hostnames = ["printer", "laptop", "phone", "camera", "iot"]
    name = f"{random.choice(hostnames)}-{random.randint(1,99)}"
    return {"ip": str(ip), "mac": mac, "name": name}
def mock_scan_network(network_cidr, positive_rate=0.05, max_results=10, delay_per_host=0.01):
    net = ipaddress.ip_network(network_cidr, strict=False)
    results = []
    for ip in net.hosts():
        # artificial delay so output feels realistic (tune or set to 0)
        if delay_per_host:
            time.sleep(delay_per_host)
        if random.random() < positive_rate:
            results.append(simulate_device(ip))
            if len(results) >= max_results:
                break
    return results
def pretty_print(devices):
    if not devices:
        print("No devices found")
        return
    print("\nActive devices found:")
    print("IP Address\t\tMAC Address\t\tName")
    print("-" * 60)
    for d in devices:
        print(f"{d['ip']}\t{d['mac']}\t{d['name']}")

if __name__ == "__main__":
    network = "192.168.1.0/24"      # adjust for simulation only
    print(f"Simulated scanning network: {network}\n")
    devices = mock_scan_network(network, positive_rate=0.08, max_results=8, delay_per_host=0.005)
    pretty_print(devices)
