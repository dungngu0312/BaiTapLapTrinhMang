import socket
import sys

if len(sys.argv) != 4:
    print("Sử dụng: tcp_server <cổng> <tệp tin chứa câu chào> <tệp tin lưu nội dung client gửi đến>")
    sys.exit(1)

# lấy cổng và tên file chứa câu chào và tên file để lưu nội dung client gửi đến từ tham số dòng lệnh
port = int(sys.argv[1])
hello_file = sys.argv[2]
data_file = sys.argv[3]

# mở file chứa câu chào
with open(hello_file, 'r') as f:
    hello_msg = f.read()

# tạo socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# gán địa chỉ và cổng cho socket
server_address = ('', port)
sock.bind(server_address)

# lắng nghe kết nối từ client
sock.listen(1)
print(f"Đang lắng nghe kết nối ở cổng {port}")

while True:
    # chấp nhận kết nối từ client
    conn, addr = sock.accept()
    print(f"Đã kết nối từ {addr[0]}:{addr[1]}")

    try:
        # gửi câu chào đến client
        conn.sendall(hello_msg.encode())

        # mở file để lưu nội dung client gửi đến
        with open(data_file, 'wb') as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)

        # thông báo đã lưu xong nội dung client gửi đến
        print(f"Đã lưu nội dung từ {addr[0]}:{addr[1]} vào tệp tin {data_file}")

    finally:
        # đóng kết nối
        conn.close()
