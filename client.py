# นางสาวอาทิมา ธรรมานุรักษ์กุล 6309650171 
# นางสาวนงนภัส วงศ์ปิยะชัย 6309650734 
# นางสาวกฤติยาภรณ์ โพโส 6309650791 

import socket

# HOST = 'localhost'

# create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client connects to server
s.connect((socket.gethostname(), 8080))

while True:
    print("sending data to server")
    message = input("sended: ")
    s.send(message.encode())
    print("waiting for response")
    s_message = s.recv(1024)
    print("received:", s_message.decode())

# user_pass = "5609610760:0706"
# req_number = "NTYwOTYxMDc2MC4wNzA2LmtleQ==:request secret number:5:221"
# check_msg = "NTYwOTYxMDc2MC4wNzA2LmtleQ==:check secret number:43"
# quit = "NTYwOTYxMDc2MC4wNzA2LmtleQ==:quit"