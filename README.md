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

# **Features of the Implemented Middleware**

This document highlights the features of the implemented RMI middleware for **primitive data types** and **train ticket booking**.

---

## **General Middleware Features**
1. **Custom RMI Implementation**:
   - Built from scratch to handle client-server communication using sockets and JSON serialization.

2. **Dynamic Method Invocation**:
   - Server resolves and executes methods dynamically based on the client's request.

3. **Lightweight Protocol**:
   - Communication relies on JSON, making it simple and easily debuggable.

4. **Error Handling**:
   - Responds gracefully to invalid method calls or argument mismatches.

---

## **Features of Primitive Data Type Middleware (Part 1)**

1. **Supported Methods**:
   - `add(a, b)`: Adds two integers.
   - `multiply(a, b)`: Multiplies two floats.
   - `is_even(num)`: Checks if an integer is even.
   - `to_upper(text)`: Converts a string to uppercase.
   - `reverse_list(items)`: Reverses a list of strings.

2. **Interactive Client Interface**:
   - User-friendly CLI with options to invoke the above methods.

3. **Error Handling**:
   - Returns descriptive error messages for invalid input.

---

## **Features of Train Ticket Booking Middleware (Part 2)**

1. **Train and Ticket Management**:
   - Supports CRUD-like operations for trains and tickets:
     - Add a train.
     - Book a ticket.
     - Unbook a ticket.
     - Query tickets by train ID or departure date.

2. **Interactive Client Interface**:
   - CLI to interact with the train reservation system.

3. **Error Handling**:
   - Detects and responds to edge cases like invalid train IDs or ticket operations.

4. **Scalability**:
   - Designed to handle multiple trains, tickets, and clients.

---

## **Comparison with Pyro5 Middleware**

| **Feature**                | **Manual Middleware**                  | **Pyro5 Middleware**               |
|----------------------------|----------------------------------------|------------------------------------|
| **Ease of Use**            | Manual effort for socket handling      | Simplified with built-in features |
| **Dynamic Invocation**     | Fully implemented manually             | Built-in with Pyro5               |
| **Serialization**          | Custom JSON serialization              | Pyro5's object serialization      |
| **Extensibility**          | Fully customizable                     | Extensible with Pyro5 features    |
| **Error Handling**         | Custom error responses                 | Standardized in Pyro5             |

---

This middleware demonstrates flexibility and scalability, allowing further extensions for advanced features like persistence, authentication, or distributed systems.

## **Conclusion**

This project demonstrates the flexibility and scalability of a custom RMI middleware to handle both primitive data operations and a real-world use case like train ticket booking. Each part is modular, allowing further extensions or adaptations.
