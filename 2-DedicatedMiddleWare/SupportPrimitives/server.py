import socket
import json

class PrimitiveTypeServer:
    def add(self, a: int, b: int) -> int:
        return a + b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def is_even(self, num: int) -> bool:
        return num % 2 == 0

    def to_upper(self, text: str) -> str:
        return text.upper()

    def reverse_list(self, items: list) -> list:
        return items[::-1]

    def handle_request(self, request):
        try:
            data = json.loads(request)
            method_name = data["method"]
            args = data["args"]
            method = getattr(self, method_name)
            result = method(*args)
            return json.dumps({"status": "success", "result": result})
        except Exception as e:
            return json.dumps({"status": "error", "message": str(e)})

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("server", 9080))
    server_socket.listen(5)
    print("Primitive Type Server is running on port 9080...")

    primitive_server = PrimitiveTypeServer()

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        request = client_socket.recv(1024).decode("utf-8")
        response = primitive_server.handle_request(request)
        client_socket.send(response.encode("utf-8"))
        client_socket.close()

if __name__ == "__main__":
    server()
