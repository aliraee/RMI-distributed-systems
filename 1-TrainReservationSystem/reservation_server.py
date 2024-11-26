import Pyro5.api


@Pyro5.api.expose
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


def main():
    daemon = Pyro5.server.Daemon(host="server", port=9091)  # Start the Pyro5 daemon
    ns = Pyro5.api.locate_ns()  # Locate the Pyro5 name server
    uri = daemon.register(ReservationServer)  # Register the ReservationServer class
    ns.register("reservation.server", uri)  # Register the server with a name
    print("Train Reservation Server is ready.")
    daemon.requestLoop()  # Keep the server running

if __name__ == "__main__":
    main()
