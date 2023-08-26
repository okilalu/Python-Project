# import socket
# import json
# from Savoir import Savoir

# # Define the server IP address and port
# server_ip = socket.gethostbyname(socket.gethostname())
# server_port = 5500

# # Multichain connection parameters
# multichain_host = "localhost"
# multichain_port = 12345
# multichain_user = "multichainrpc"
# multichain_pass = "password"
# multichain_chain = "chain1"

# # Create a socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to the IP address and port
# server_socket.bind((server_ip, server_port))

# # Listen for incoming connections
# server_socket.listen(5)

# print('Node Admin is running and waiting for connections...')

# # Connect to Multichain using JSON-RPC
# multichain = Savoir(
#     multichain_host, multichain_port, multichain_user, multichain_pass, multichain_chain)

# while True:
#     # Accept a client connection
#     client_socket, client_address = server_socket.accept()
#     print('Connected to client:', client_address)

#     # Receive data from the client
#     data = client_socket.recv(1024).decode()
#     print('Received data:', data)

#     # Process the data and control the smart home
#     # Implement your smart home logic here

#     # Send response back to the client
#     response = 'Node Admin received the data'
#     client_socket.send(response.encode())

#     # Store data on Multichain
#     try:
#         # Prepare the data to be stored
#         data_to_store = {
#             "source": client_address[0],
#             "data": data
#         }

#         # Convert data to JSON format
#         data_json = json.dumps(data_to_store)

#         # Store data on Multichain
#         multichain.publish(multichain_chain, "", data_json)

#     except Exception as e:
#         print("Error while storing data on Multichain:", e)

#     # Close the connection with the client
#     client_socket.close()


import socket
import json

# Define the server IP address and port
server_ip = socket.gethostbyname(socket.gethostname())
server_port = 5500
HEADER = 4096

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(5)

print('Node Admin is running and waiting for connections...')

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print('Connected to client:', client_address)

    # Receive data from the client
    data = client_socket.recv(HEADER).decode("utf-8")
    print('Received data:', data)

    # Process the data and control the smart home
    # Implement your smart home logic here

    # Convert data to JSON format
    # data_json = json.dumps(data)

    # Send response back to the client
    response = 'Node Admin received the data'
    client_socket.send(response.encode())

    # Close the connection with the client
    client_socket.close()
