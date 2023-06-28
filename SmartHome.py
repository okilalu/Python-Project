import random
import time
import socket

# Definisikan IP address dan port server

HEADER = 64
# PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# SERVER = "192.168.88.1"
server_ip = "192.168.88.1"
server_port = 5000
ADDR = (server_ip, server_port)

# Definisikan keadaan awal smart home
lampu_hidup = False
suhu = 20.0
kelembaban = 50.0
gerakan_terdeteksi = False

# Buat socket object untuk berkomunikasi dengan server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Terhubung ke server
client_socket.connect((server_ip, server_port))

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
    print("Jam: {:02d}:00, Lampu: {}, Suhu: {:.1f}C, Kelembaban: {:.1f}%, Gerakan Terdeteksi: {}".format(
        jam, "Hidup" if lampu_hidup else "Mati", suhu, kelembaban, gerakan_terdeteksi))

    # Kirim data ke server
    message = "Jam: {:02d}:00, Lampu: {}, Suhu: {:.1f}C, Kelembaban: {:.1f}%, Gerakan Terdeteksi: {}".format(
        jam, "Hidup" if lampu_hidup else "Mati", suhu, kelembaban, gerakan_terdeteksi)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client_socket.send(send_length)
    client_socket.send(message.encode())

    # Tunggu 1 detik untuk mewakili waktu berjalan
    time.sleep(1)

# Tutup koneksi dengan server
client_socket.close()
