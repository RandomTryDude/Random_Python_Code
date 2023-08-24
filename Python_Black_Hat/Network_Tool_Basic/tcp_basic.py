import socket

target_host = "127.0.0.1" # adresse d'envoie
target_port = 9998 # port d'écoute

#create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET == IPV4
# SOCK_STREAM == client TCP

# connect the client
client.connect((target_host,target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")
# message envoyé

# receive some data

response = client.recv(4096)
# recois réponse de notre serveur

print(response.decode())
client.close()
