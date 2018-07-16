import argparse
import json
import socket
import threading
from threading import Thread

import random
import time


def getIPAddresses():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipadd = s.getsockname()[0]
    s.close()
    return ipadd


def clientUDP(name):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("CLIENT UDP")
    msg = ("Hello you there! I'm %s" % name).encode(
        'utf-8')  # socket.sendto() takes bytes as input, hence we must encode the string first.
    s.sendto(msg, ('localhost', 60008))
    print("UDP client > %s  IP: %s" % s.recvfrom(8192))


def serverUDP(client_list):
    sudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sudp.bind(('localhost', 60008))
    print("\tUDP..SOCK_DGRAM..connection has been set up Port:%s" % 60008)
    while True:
        msg, addr = sudp.recvfrom(8192)  # This is the amount of bytes to read at maximum
        print("UDP>Got message from UDP %s: %s" % (addr, msg.decode()))
        # client_list[addr]=msg
        sudp.sendto("Got your message!".encode(), addr)  # Send reply


def handle_client(client_list, conn, address):
    print(conn)
    name = conn.recv(1024)
    name_str = name.decode()
    client_list[name] = json.dumps(dict(zip(['name', 'address', 'port'], [name_str, address[0], address[1]])),
                                   ensure_ascii=True)
    a = ''
    for nam in client_list:
        a += str(client_list[nam])
    print(a)
    conn.sendall(str.encode(client_list[name]))
    # conn.shutdown(socket.SHUT_RDWR)
    #  conn.close()
    ripeti = 1
    while ripeti == 1:
        data = conn.recv(1024).decode()
        print("\tTCP/Client/%s/Data/%s" % (name_str, data))
        if "#!END!#" in data:
            print("TCP>Closing the connection %s" % name_str)
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
            ripeti = 0


def serverTCP(client_list):
    HOST = ''  # localhost
    PORT = 50008
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create an INET, STREAMing socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))  # bind to that port
    s.listen(5)  # listen for user input and accept 5 connection at a time.
    print('\tTCP.SOCK_STREAM...connection has been set up Port:%s' % PORT)

    while True:
        (conn, address) = s.accept()
        t = threading.Thread(target=handle_client, args=(client_list, conn, address))
        t.daemon = True
        t.start()


def clientTCP(name):
    print('Starting client..socket.SOCK_STREAM..... TCP')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.255.10', 50008))
    rip = random.randint(1, 10)
    print('NAME %s %s' % (name, rip))
    time.sleep(rip)
    name_bytes = str.encode(name)

    s.send(name_bytes)
    data = s.recv(1024)
    result = json.loads(data.decode())
    print(json.dumps(result, indent=4))
    while rip > 0:
        s.send(str.encode(str(rip)))
        rip -= 1
        print(rip)
        time.sleep(rip)
    s.send(str.encode("#!END!#"))


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', dest='client', action='store_true')
    parser.add_argument('-n', dest='name', type=str, default='name')
    parser.add_argument('-cs', dest='clients', action='store_true')
    result = parser.parse_args()
    return result


def main():
    # When run with no arguments, this program starts a TCP socket server that listens for connections to 127.0.0.1 on
    client_list = dict()
    args = parse_arguments()
    threads = []
    if args.clients:
        for page_num in range(1, 18):
            t = Thread(target=clientTCP, args=(str(page_num),), daemon=True)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    elif args.client:
        # Client TCP
        t = Thread(target=clientTCP, args=(args.name,), daemon=True)
        t.start()
        threads.append(t)
        # Client UPD
        t = Thread(target=clientUDP, args=(args.name,), daemon=True)
        t.start()
        threads.append(t)

    else:
        try:
            # Server  TCP &UDP
            hostname = socket.gethostname()
            ip = str(socket.gethostbyname(hostname))
            print('Starting server..socket.Hostname %s  (Ip: %s - %s ) ....' % (hostname, ip, getIPAddresses()))
            t = Thread(target=serverTCP, args=(client_list,), daemon=True)
            t.start()
            threads.append(t)
            # Server UPD
            t = Thread(target=serverUDP, args=(client_list,), daemon=True)
            t.start()
            threads.append(t)
        except KeyboardInterrupt:
            print("Keyboard interrupt")

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
