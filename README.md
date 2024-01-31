# Socket Programming

Developed socket programming to simulate a communication method, allowing processes or programs running on different devices to exchange data seamlessly through a network

### Server Side:
#### 1. Import Necessary Libraries:
```
import socket
```
#### 2. Create a Server Socket:
Create a server socket using the socket() function
```
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
#### 3. Bind the Socket:
Bind the server socket to a specific address and port
```
s.bind(socket.gethostname(), 8080)
```
#### 4. Listen for Connections:
Enable the server socket to listen for incoming connections
```
# wait for connection from client
s.listen()
```
#### 5. Accept Connections:
Accept incoming connections and establish a connection with the client
```
# get connection from client
connection, client_address = s.accept()
```

### Client Side:
#### 1. Import Necessary Libraries:
```
import socket
```
#### 2. Create a Client Socket:
Create a client socket using the socket() function
```
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
#### 3. Connect to Server:
Connect the client socket to the server's address and port.
```
s.connect(socket.gethostname(), 8080)
```
#### 4. Send and Receive Data:
Use the client socket to send and receive data
```
# Sending data
message = input("sended: ")
s.send(message.encode())

# Receiving data
s_message = s.recv(1024)
print("received:", s_message.decode())
```

---

### 🪚 Tools Used:
![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Visual Studio Code Badge](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
