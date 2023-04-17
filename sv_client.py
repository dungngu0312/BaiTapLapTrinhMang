import socket

server_address = ('localhost', 9999)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

mssv = input('MSSV: ')
hoten = input('Họ tên: ')
ngaysinh = input('Ngày sinh: ')
diemtb = input('Điểm trung bình các môn học: ')

data = f'{mssv},{hoten},{ngaysinh},{diemtb}'

client_socket.sendall(data.encode('utf-8'))

client_socket.close()
