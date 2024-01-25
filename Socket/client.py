import socket   

BUFF_SIZE = 512 # Byte

print("Client Dosyası çalışıtırıldı.")
"""
socket.socket(AdreslemeSekli,İletisimTipi)

AF_INET : 192.0.2.235  ipv4
AF_INET6 : 2001:DB8:ABCD:12::   ipv6
AF_UNIX : UNİX İpleri için kullanılıyor.

SOCK_DGRAM : UDP
SOCK_STREAM : TCP
"""
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

"""
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)

IPPROTO_IP : İstek IP protokol katmanına uygulanır.
IPPROTO_TCP : İstek, TCP protokol katmanına uygulanır.
SOL_SOCKET : İstek soket katmanı için geçerlidir.
IPPROTO_IPV6 : İstek IPv6 protokol katmanı için geçerlidir.
IPPROTO_ICMPV6 : İstek ICMPv6 protokol katmanı için geçerlidir.

SO_RCVBUF : Alma arabelleğinin boyutunu ayarla.
"""

client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)

host_ip = 'localhost' # 127.0.0.1
port = 9998
message = b'clientten geldim'

client_socket.sendto(message,(host_ip,port))

packet,_ = client_socket.recvfrom(BUFF_SIZE)
print("Server'dan gelen mesaj : ",packet)

    
    


    

