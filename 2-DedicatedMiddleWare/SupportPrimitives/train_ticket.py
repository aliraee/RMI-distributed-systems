class TrainTicket:
    def __init__(self, ticket_id, train_id, passenger_name, seat_type):
        self.ticket_id = ticket_id
        self.train_id = train_id
        self.passenger_name = passenger_name
        self.seat_type = seat_type

    def to_dict(self):
        return {
            "ticket_id": self.ticket_id,
            "train_id": self.train_id,
            "passenger_name": self.passenger_name,
            "seat_type": self.seat_type,
        }

    @staticmethod
    def from_dict(data):
        return TrainTicket(
            ticket_id=data["ticket_id"],
            train_id=data["train_id"],
            passenger_name=data["passenger_name"],
            seat_type=data["seat_type"],
        )
