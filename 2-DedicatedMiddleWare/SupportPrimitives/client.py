import socket
import json

class PrimitiveTypeClient:
    def __init__(self, host="localhost", port=9090):
        self.host = host
        self.port = port

    def send_request(self, method, *args):
        request = json.dumps({"method": method, "args": args})
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.send(request.encode("utf-8"))
            response = client_socket.recv(1024).decode("utf-8")
            return json.loads(response)

    def add(self, a, b):
        return self.send_request("add", a, b)

    def multiply(self, a, b):
        return self.send_request("multiply", a, b)

    def is_even(self, num):
        return self.send_request("is_even", num)

    def to_upper(self, text):
        return self.send_request("to_upper", text)

    def reverse_list(self, items):
        return self.send_request("reverse_list", items)

if __name__ == "__main__":
    client = PrimitiveTypeClient()

    print(client.add(5, 10))          # {"status": "success", "result": 15}
    print(client.multiply(3.2, 2.1)) # {"status": "success", "result": 6.72}
    print(client.is_even(4))         # {"status": "success", "result": true}
    print(client.to_upper("hello"))  # {"status": "success", "result": "HELLO"}
    print(client.reverse_list([1, 2, 3, 4]))  # {"status": "success", "result": [4, 3, 2, 1]}
