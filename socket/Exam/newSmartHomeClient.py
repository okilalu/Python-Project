import random
import time
import socket

# Define the server IP address and port
server_ip = "192.168.88.1"
server_port = 5500

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print('Connected to the Smart Home Controller')

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
        print("Jam: {:02d}:00, Lampu: {}, Suhu: {:.1f}C, Kelembaban: {:.1f}%, Gerakan Terdeteksi: {}".format(
            jam, "Hidup" if lampu_hidup else "Mati", suhu, kelembaban, gerakan_terdeteksi))

        data = "Jam: {:02d}:00, Lampu: {}, Suhu: {:.1f}C, Kelembaban: {:.1f}%, Gerakan Terdeteksi: {}".format(
            jam, "Hidup" if lampu_hidup else "Mati", suhu, kelembaban, gerakan_terdeteksi)

        try:
            client_socket.send(data.encode())
        except Exception as e:
            print("Error while sending data:", e)
            break

        # Tunggu 1 detik untuk mewakili waktu berjalan
        time.sleep(1)

    # Receive response dari the server
    response = client_socket.recv(1024).decode()
    print('Received response:', response)

except Exception as e:
    print("Error during the socket connection:", e)

finally:
    # Tutup koneksi dengan server
    client_socket.close()
