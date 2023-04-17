import socket
import datetime

server_address = ('localhost', 9999)
log_file = 'sv_log.txt'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024).decode('utf-8')
    
    now = datetime.datetime.now()
    log_data = f'{client_address[0]}, {now.strftime("%Y-%m-%d %H:%M:%S")}, {data}'
    
    print(log_data)
    
    with open(log_file, 'a') as f:
        f.write(log_data + '\n')
        
    client_socket.close()
