import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 0.0.0.0 escuchar desde cualquier interfaz(red) de la computadora 
s.bind(("0.0.0.0", 1337))
s.listen(1)
conn, addr = s.accept()
with conn:
    dataFromClient = conn.recv(1024)
    print(dataFromClient)
    #lo que mandas 
    conn.send(b"OK")