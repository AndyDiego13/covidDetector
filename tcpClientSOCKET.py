import socket

#función socket (tipo de socket "se indico que era un socket de internet de capa 3" , stream es para el tipo de protocolo STREAM es TCP )
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#sock.SOCK_DGRAM
#el 80 es para decir que se enviará la request con http
s.connect(("127.0.0.1", 80))
#b es el socket de a.coneect, que se estará enviando 
s.send(b'GET / HTTP/1.1\r\n\r\n')

#arriba estas mandando la solicitud para recibir datos de pa pagina

#esos datos que de arriba que se enviaron se deben recibir
#dijo que se recibiran 1024 datos nomas porque si
data=s.recv(1024)
print(data)
s.close()