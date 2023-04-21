##########
#
#   Author: Aurélien LOHMANN
#
##########

import socket
import pickle
import time


def get_event_data():
    # Replace this function with the code to read data.
    event_data = [
        {'x': 10, 'y': 20, 'timestamp': time.time(), 'polarity': 1},
        {'x': 15, 'y': 25, 'timestamp': time.time(), 'polarity': 0},
    ]
    return event_data


def main():
    # Configuration
    host = '0.0.0.0'  # Listen on all available network interfaces
    port = 12345       # Choose an appropriate port number

    # Create a socket and bind it to the host and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for up to 5 pending connections

    print(f"Server listening on {host}:{port}")

    try:
        while True:
            # Accept a client connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            try:
                while True:
                    # Get event data from the event camera
                    event_data = get_event_data()

                    # Serialize the event data using pickle
                    serialized_data = pickle.dumps(event_data)

                    # Send the serialized data to the client
                    client_socket.sendall(serialized_data)

                    # Wait before sending the next set of event data
                    time.sleep(0.01)
            except (ConnectionResetError, BrokenPipeError):
                print(f"Connection closed by {client_address}")
            finally:
                client_socket.close()

    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
