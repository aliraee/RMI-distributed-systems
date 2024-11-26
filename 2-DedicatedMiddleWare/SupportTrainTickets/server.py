import socket
import json


class ReservationServer:
    def __init__(self):
        # Dictionary to hold train and ticket information
        self.trains = {}  # {train_id: {"origin": str, "destination": str, "departure": str, "tickets": []}}

    def add_train(self, train_id, origin, destination, departure):
        """Add a new train."""
        if train_id in self.trains:
            return f"Train {train_id} already exists."
        self.trains[train_id] = {
            "origin": origin,
            "destination": destination,
            "departure": departure,
            "tickets": []
        }
        return f"Train {train_id} added successfully."

    def book_ticket(self, train_id, seat_type, passenger_name):
        """Book a ticket for a train."""
        if train_id not in self.trains:
            return f"Train {train_id} does not exist."
        ticket_id = len(self.trains[train_id]["tickets"]) + 1
        self.trains[train_id]["tickets"].append({
            "ticket_id": ticket_id,
            "seat_type": seat_type,
            "passenger_name": passenger_name
        })
        return f"Ticket {ticket_id} booked successfully for {passenger_name} in {seat_type} class."

    def unbook_ticket(self, train_id, ticket_id):
        """Unbook a ticket for a train."""
        if train_id not in self.trains:
            return f"Train {train_id} does not exist."
        tickets = self.trains[train_id]["tickets"]
        for ticket in tickets:
            if ticket["ticket_id"] == ticket_id:
                tickets.remove(ticket)
                return f"Ticket {ticket_id} successfully unbooked."
        return f"Ticket {ticket_id} not found for train {train_id}."

    def get_tickets_by_train_id(self, train_id):
        """Get all tickets for a specific train."""
        if train_id not in self.trains:
            return f"Train {train_id} does not exist."
        return self.trains[train_id]["tickets"]

    def get_tickets_by_date(self, date):
        """Get all tickets for trains departing on a specific date."""
        tickets = []
        for train_id, train_info in self.trains.items():
            if train_info["departure"].startswith(date):
                tickets.extend(train_info["tickets"])
        return tickets

    def handle_request(self, request):
        """Handle client requests."""
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
    """Start the Reservation Server."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9090))
    server_socket.listen(5)
    print("Reservation Server is running on port 9090...")

    reservation_server = ReservationServer()

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        request = client_socket.recv(1024).decode("utf-8")
        response = reservation_server.handle_request(request)
        client_socket.send(response.encode("utf-8"))
        client_socket.close()


if __name__ == "__main__":
    server()
