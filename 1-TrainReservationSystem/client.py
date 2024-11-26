import Pyro5.api

def main():
    server = Pyro5.api.Proxy("PYRONAME:reservation.server")  # Connect to the server

    while True:
        print("\n--- Train Reservation System ---")
        print("1. Add Train")
        print("2. Book Ticket")
        print("3. Unbook Ticket")
        print("4. Get Tickets by Train ID")
        print("5. Get Tickets by Date")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            train_id = input("Train ID: ")
            origin = input("Origin: ")
            destination = input("Destination: ")
            departure = input("Departure (YYYY-MM-DD HH:MM): ")
            print(server.add_train(train_id, origin, destination, departure))
        elif choice == "2":
            train_id = input("Train ID: ")
            seat_type = input("Seat Type (economy/business): ")
            passenger_name = input("Passenger Name: ")
            print(server.book_ticket(train_id, seat_type, passenger_name))
        elif choice == "3":
            train_id = input("Train ID: ")
            ticket_id = int(input("Ticket ID: "))
            print(server.unbook_ticket(train_id, ticket_id))
        elif choice == "4":
            train_id = input("Train ID: ")
            print(server.get_tickets_by_train_id(train_id))
        elif choice == "5":
            date = input("Date (YYYY-MM-DD): ")
            print(server.get_tickets_by_date(date))
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
