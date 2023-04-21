##########
#
#   Author: Aurélien LOHMANN
#
##########

import socket
import pickle


def process_event_data(event_data):
    # Process the received event data
    print("Received event data:", event_data)


def main():
    # Configuration
    server_ip = '127.0.0.1'  # Replace with the IP address of the server
    server_port = 12345      # The same port number as the server

    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server at {server_ip}:{server_port}")

    try:
        while True:
            # Receive serialized data from the server
            serialized_data = b''
            while True:
                chunk = client_socket.recv(4096)
                if not chunk:
                    break
                serialized_data += chunk

                # Check if the serialized data is complete
                try:
                    event_data = pickle.loads(serialized_data)
                    break
                except EOFError:
                    # If the data is incomplete, keep receiving more data
                    continue

            # Deserialize and process the event data
            process_event_data(event_data)

    except KeyboardInterrupt:
        print("\nClient disconnecting.")
    finally:
        client_socket.close()


if __name__ == '__main__':
    main()
