# RMI-distributed-systems
RMI Distributed Systems - Fall 2024 at CE AUT
# Train Ticket Reservation System with Pyro5 - First Phase  

This project is a **distributed train ticket reservation system** implemented in Python using the **Pyro5 library** for Remote Method Invocation (RMI). It allows clients to interact with a remote server to manage train schedules and reservations seamlessly.

---

## Features

### Server-Side Features:
- **Add Trains**: Add new trains with details such as train ID, origin, destination, and departure time.
- **Book Tickets**: Reserve tickets for passengers, specifying the seat type (e.g., economy, business) and passenger name.
- **Unbook Tickets**: Cancel reservations using ticket IDs.
- **Query Tickets by Train ID**: Retrieve all tickets for a specific train.
- **Query Tickets by Date**: Retrieve all tickets for trains departing on a given date.

### Client-Side Features:
- A text-based menu for users to interact with the server to:
  - Add trains.
  - Book or unbook tickets.
  - Query tickets by train ID or departure date.

### RMI Features:
- **Remote Invocation**: The server methods are exposed remotely, allowing clients to invoke them as though they are local.
- **Concurrent Access**: Multiple clients can interact with the server simultaneously.

---

## Technologies Used
- **Python 3.10+**
- **Pyro5**: Simplifies remote method invocation by managing communication and object serialization.

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aliraee/RMI-distributed-systems.git
   cd train-reservation-system

# RMI Middleware Project - Phase 2
<!-- ## Part 1: Supporting Primitive Data Types -->
[Part 1: Supporting Primitive Data Types](2-DedicatedMiddleWare/SupportPrimitives/README.md)

<!-- ## Part 2: Supporting Train Ticket Booking -->

[Part 2: Supporting Train Ticket Booking](2-DedicatedMiddleWare/SupportTrainTickets/README.md)

## **Conclusion**

This project demonstrates the flexibility and scalability of a custom RMI middleware to handle both primitive data operations and a real-world use case like train ticket booking. Each part is modular, allowing further extensions or adaptations.
