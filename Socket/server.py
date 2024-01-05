import socket



BUFF_SIZE = 512 # Byte

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)

host_name = socket.gethostname()

socket_address = ('localhost',9998)

server_socket.bind(socket_address)


msg,client_addr = server_socket.recvfrom(BUFF_SIZE)

message = b"serverdan geldim"

server_socket.sendto(message,client_addr)

print("Clientten gelen mesaj : ",str(msg))
	
        

        