import socket
import json


class ReservationClient:
    def __init__(self, host="server", port=9070):
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

    def add_train(self, train_id, origin, destination, departure):
        return self.send_request("add_train", train_id, origin, destination, departure)

    def book_ticket(self, train_id, seat_type, passenger_name):
        return self.send_request("book_ticket", train_id, seat_type, passenger_name)

    def unbook_ticket(self, train_id, ticket_id):
        return self.send_request("unbook_ticket", train_id, ticket_id)

    def get_tickets_by_train_id(self, train_id):
        return self.send_request("get_tickets_by_train_id", train_id)

    def get_tickets_by_date(self, date):
        return self.send_request("get_tickets_by_date", date)


def main():
    client = ReservationClient()

    while True:
        print("\n--- Train Reservation System ---")
        print("1. Add Train")
        print("2. Book Ticket")
        print("3. Unbook Ticket")
        print("4. Get Tickets by Train ID")
        print("5. Get Tickets by Date")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                train_id = input("Train ID: ")
                origin = input("Origin: ")
                destination = input("Destination: ")
                departure = input("Departure (YYYY-MM-DD HH:MM): ")
                response = client.add_train(train_id, origin, destination, departure)
                print("Server Response:", response["result"])

            elif choice == "2":
                train_id = input("Train ID: ")
                seat_type = input("Seat Type (economy/business): ")
                passenger_name = input("Passenger Name: ")
                response = client.book_ticket(train_id, seat_type, passenger_name)
                print("Server Response:", response["result"])

            elif choice == "3":
                train_id = input("Train ID: ")
                ticket_id = int(input("Ticket ID: "))
                response = client.unbook_ticket(train_id, ticket_id)
                print("Server Response:", response["result"])

            elif choice == "4":
                train_id = input("Train ID: ")
                response = client.get_tickets_by_train_id(train_id)
                print("Tickets:", response["result"])

            elif choice == "5":
                date = input("Date (YYYY-MM-DD): ")
                response = client.get_tickets_by_date(date)
                print("Tickets:", response["result"])

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    main()
