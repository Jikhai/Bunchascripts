#!/usr/bin/python3

import os
import sys 
import socket

def main():

    if len(sys.argv) <2 :
        print ("Usage : [link]")
        sys.exit(1)

    goal = sys.argv[1]

    try : 
        liste = socket.getaddrinfo(goal,"http",0,socket.SOCK_STREAM)
    except Exception as err:
        print("Failure ! -->", err)
        sys.exit(1)


    for a in liste :
        (family, type, proto, name, sockaddr) = a
        lesocket = socket.socket(family, type, proto)
    
        try :
            lesocket.connect(sockaddr)
        except Exception as err:
            print("Failure ! -->", err," :", sockaddr)
            continue

        break
    else:
        sys.exit(1)

        
    try :
        lesocket.send(b"GET /\r\n\r\n")
    except Exception as err:
        print("Failure ! -->", err)
        sys.exit(1)
    
    while True :
        if lesocket.recv(256) == b'' :
            break
        print(lesocket.recv(256))

if __name__ == "__main__":
    main()
