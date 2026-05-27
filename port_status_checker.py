import socket

host = input("Which website or IP should we check? ")
port = int(input("Which port number? "))

print(f"Checking {host}...")

connection_tool = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_tool.settimeout(2)

status = connection_tool.connect_ex((host, port))

if status == 0:
    print("The port is OPEN!")
else:
    print("The port is CLOSED.")

connection_tool.close()