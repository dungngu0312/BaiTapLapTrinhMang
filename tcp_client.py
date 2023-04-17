import socket
import sys

# Kiểm tra đối số dòng lệnh
if len(sys.argv) != 3:
    print("Sử dụng: tcp_client <địa chỉ IP> <cổng>")
    sys.exit(1)

# Lấy địa chỉ IP và cổng từ tham số dòng lệnh
server_address = (sys.argv[1], int(sys.argv[2]))

# Tạo socket và kết nối đến máy chủ
print(f"Đang kết nối đến {server_address[0]}:{server_address[1]}")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)

# Gửi dữ liệu đến máy chủ và nhận phản hồi
while True:
    data = input("Nhập dữ liệu: ")
    sock.sendall(data.encode())
    if data == 'exit':
        break
    response = sock.recv(1024).decode()
    print("Phản hồi từ máy chủ:", response)

# Đóng kết nối và socket
print("Kết thúc kết nối")
sock.close()
