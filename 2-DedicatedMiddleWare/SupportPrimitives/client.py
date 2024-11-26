import socket
import json


class PrimitiveTypeClient:
    def __init__(self, host="localhost", port=9090):
        self.host = host
        self.port = port

    def send_request(self, method, *args):
        """Send a request to the server and receive the response."""
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


def main():
    client = PrimitiveTypeClient()

    while True:
        print("\n--- Primitive Type Operations ---")
        print("1. Add Two Numbers")
        print("2. Multiply Two Numbers")
        print("3. Check if a Number is Even")
        print("4. Convert Text to Uppercase")
        print("5. Reverse a List")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                response = client.add(a, b)
                print("Result:", response["result"])

            elif choice == "2":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                response = client.multiply(a, b)
                print("Result:", response["result"])

            elif choice == "3":
                num = int(input("Enter a number: "))
                response = client.is_even(num)
                print("Is Even:", response["result"])

            elif choice == "4":
                text = input("Enter text: ")
                response = client.to_upper(text)
                print("Uppercase Text:", response["result"])

            elif choice == "5":
                items = input("Enter list items separated by spaces: ").split()
                response = client.reverse_list(items)
                print("Reversed List:", response["result"])

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    main()
