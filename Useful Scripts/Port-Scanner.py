import socket
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm


class PortScanner:
    def __init__(self, target, start_port=1, end_port=1024, max_workers=100):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.max_workers = max_workers
        self.open_ports = []

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((self.target, port))
                if result == 0:
                    self.open_ports.append(port)
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    def scan(self):
        print(
            f"Scanning {self.target} from port {self.start_port} to {self.end_port}..."
        )
        total_ports = self.end_port - self.start_port + 1

        with tqdm(total=total_ports, desc="Scanning Ports", unit="port") as progress:
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = []
                for port in range(self.start_port, self.end_port + 1):
                    future = executor.submit(self.scan_port, port)
                    future.add_done_callback(lambda p: progress.update())
                    futures.append(future)

                for future in futures:
                    future.result()

        if self.open_ports:
            print(f"Open ports on {self.target}:")
            for port in self.open_ports:
                print(f"Port {port} is open")
        else:
            print(
                f"No open ports found on {self.target} in the range {self.start_port}-{self.end_port}."
            )


def get_validated_port(prompt, default):
    while True:
        response = input(prompt)
        if not response:
            return default
        if response.isdigit():
            return int(response)
        else:
            print("Please enter a valid number.")


if __name__ == "__main__":
    target = input("Enter the target IP address or hostname: ")
    start_port = get_validated_port("Enter the start port (default 1): ", 1)
    end_port = get_validated_port("Enter the end port (default 1024): ", 1024)
    scanner = PortScanner(target, start_port, end_port)
    scanner.scan()
