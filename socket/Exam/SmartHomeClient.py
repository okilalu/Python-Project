import random
import time
import socket
import json

# Define the server IP address and port
server_ip = "192.168.88.1"
# server_ip = socket.gethostbyname(socket.gethostname())
server_port = 5500
HEADER = 4096

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))
print('Connected to the Node Admin')

complate_data = " "

# Send data to the server
# data = 'Temperature: 25C, Lights: On'
# client_socket.send(data.encode())

# Implement code of Smart Home
lampu_hidup = False
suhu = 20.0
kelembaban = 50.0
gerakan_terdeteksi = False

# Simulasikan satu hari di smart home
for jam in range(24):
    # Simulasikan data sensor
    suhu += random.uniform(-1.0, 1.0)
    kelembaban += random.uniform(-5.0, 5.0)
    gerakan_terdeteksi = random.choice([True, False])

    # Simulasikan respon smart home terhadap data sensor
    if jam >= 6 and jam < 8:
        # Nyalakan lampu pada pagi hari
        lampu_hidup = True
    elif jam >= 18 and jam < 22:
        # Nyalakan lampu pada malam hari
        lampu_hidup = True
    else:
        # Matikan lampu pada malam hari
        lampu_hidup = False

    if gerakan_terdeteksi:
        # Tingkatkan suhu dan kelembaban ketika ada gerakan terdeteksi
        suhu += 1.0
        kelembaban += 10.0

    # Tampilkan keadaan terkini dari smart home
    # print("Jam: {:02d}:00, Lampu: {}, Suhu: {:.1f}C, Kelembaban: {:.1f}%, Gerakan Terdeteksi: {}".format(
    #     jam, "Hidup" if lampu_hidup else "Mati", suhu, kelembaban, gerakan_terdeteksi))

    # data = {
    #     "Jam": jam,
    #     "lampu": "Hidup" if lampu_hidup else "Mati",
    #     "suhu": suhu,
    #     "kelembaban": kelembaban,
    #     "gerakan_terdeteksi": gerakan_terdeteksi
    # }

    # try:
    #     # Convert data to JSON format
    #     data_json = json.dumps(data)

    #     # Send JSON data to the server
    #     client_socket.send(data_json.encode())

    # except ConnectionAbortedError as e:
    #     print("Error while sending data:", e)
    #     break
    while True:
        data = "Jam: {:02d}:00, Lampu: {}, Suhu: {:.1f}C, Kelembaban: {:.1f}%, Gerakan Terdeteksi: {}".format(
            jam, "Hidup" if lampu_hidup else "Mati", suhu, kelembaban, gerakan_terdeteksi)
        if len(data) <= 0:
            break
        complate_data += data
        print(complate_data)
        client_socket.send(data.encode())

        # try:
        #     client_socket.send(data.encode())
        # except ConnectionAbortedError as e:
        #     print("Error while sending data:", e)
        #     break

        # Tunggu 1 detik untuk mewakili waktu berjalan
        time.sleep(1)

        # Receive response from the server
        response = client_socket.recv(HEADER).decode("utf-8")
        print('Received response:', response)

        # Close the connection with the server
        client_socket.close()
