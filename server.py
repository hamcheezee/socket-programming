# นางสาวอาทิมา ธรรมานุรักษ์กุล 6309650171 
# นางสาวนงนภัส วงศ์ปิยะชัย 6309650734 
# นางสาวกฤติยาภรณ์ โพโส 6309650791 

import csv
import socket
import base64

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

# loop schedule
iter1 = True 
iter2 = True
iter3 = False

# create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket successfully created")

# read the server's listening port and secret key
with open("server.config.txt") as file:
    contents = file.read()

PORT = int(contents.split("\n")[0].split("=")[1])   
SECRET_KEY = contents.split("\n")[1].split("=")[1]

# read username and password
file = open("user_pass.csv")
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

# assign basic information to a socket object
s.bind((socket.gethostname(), PORT))
print("socket binded to port", PORT)

# wait for connection from client
s.listen()

print("waiting for connection")

# get connection from client
connection, client_address = s.accept()

try:
    print("connection from", client_address)

    # get data from client
    while True:
        data = connection.recv(1024)    # set the data size to be received
        print("received:", data)

        # checking username and password from client
        count = 0

        while iter1:
            for index in range(len(rows)):
                user_pass = ':'.join([str(elem) for elem in rows[index]])   # convert to string
                
                if(user_pass.encode() == data):
                    username = user_pass.split(":")[0]
                    password = user_pass.split(":")[1]
                    
                    valid_user_pass = True
                    break
                
                else:
                    count += 1

                    if(count < 3) :
                        connection.send(str.encode("Invalid username or password " + str(count) + "/3 times"))

                    if(count >= 3):
                        valid_user_pass = False
                        connection.send(str.encode("Connection refused!! you've exceeded maximum number of attempts"))

                        connection.close()
                        break
            iter1 = False

        # send data back to the client
        if data:
            print("sending data back to the client")

            while iter2:
                if valid_user_pass:
                    message = username + "." + password + "." + SECRET_KEY

                    # converted to byte format before encoding
                    message_bytes = message.encode()

                    # encode the byte data with base64
                    base64_bytes = base64.b64encode(message_bytes)

                    # converts encoded data to string
                    base64_string = base64_bytes.decode()
                
                    reply = "token:" + base64_string
                    connection.send(str.encode(reply))
                
                else:
                    connection.send(str.encode("Connection refused!!!"))
                    break

                iter2 = False

            # checking possible 'message' values
            if('request secret number' in data.decode().split(":")[1] or 
               'check secret number' in data.decode().split(":")[1] or
               'quit' in data.decode().split(":")[1]):

                iter3 = True

                # secret number before encryption
                secret_number = 0
                for digit in str(6309650734): 
                    secret_number += int(digit)

                # verify username and password
                count = 0

                if(data.decode().split(":")[0] == base64_string):
                    connection.send(str.encode("Authenticated : true"))

                    data = connection.recv(1024)

                    # if the value 'message' == 'request secret number'
                    if(data.decode().split(":")[1] == 'request secret number'):
                        e = data.decode().split(":")[2]
                        n = data.decode().split(":")[3]

                        # calculate secret number
                        # 6309650171 = 38
                        # 6309650734 = 43
                        # 6309650791 = 46

                        secret_number = 0
                        for digit in str(6309650734): 
                            secret_number += int(digit)

                        cipher_text = ((secret_number ** int(e)) % int(n))

                        c_reply = "Encrypted Secret Number:" + str(cipher_text)
                        connection.send(str.encode(c_reply))

                    # if the value 'message' == 'check secret number'
                    if(data.decode().split(":")[1] == 'check secret number'):
                        sn = data.decode().split(":")[2]
                        
                        if(int(sn) == secret_number):
                            connection.send(str.encode("Secret Number Verification: true"))

                        else:
                            connection.send(str.encode("Secret Number Verification:false"))
                    
                    # if the value 'message' == 'quit'
                    if(data.decode().split(":")[1] == 'quit'):
                        connection.send(str.encode("Session is closed."))

                        connection.close()
                        break
                
                else:
                    count += 1
                    connection.send(str.encode("Authenticated :false"))

                    if(count >= 3):
                        connection.send(str.encode("Connection refused!! you've provided wrong tokens 3 times in a row"))

                        connection.close()
                        break

            else:
                if(iter3):
                    connection.send(str.encode("Connection refused !! Invalid Action."))

                    connection.close()
                    break

        # if there is no data, wait for the data to end
        else: 
            print("no more data from", client_address)
            break
    
# after receiving the data, close the connection
finally:
    connection.close()
    print("closed connection")