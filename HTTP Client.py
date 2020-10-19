# Simon Oh
# Create a HTTP server

import socket

serverName = "ho587"
contentLength = 0
serverPort = 8080
numRequest = 0
home = '<HTML><HEAD><TITLE>HTTP Homework</TITLE></HEAD> <BODY><H3><CENTER>HTTP Homework</CENTER></H3>This is the main page<P>You can click on <A HREF=”/page2”>page 2</A> or <A HREF=”/page3”>or Page 3</A><P><CENTER>This server has been used XXX times</CENTER></BODY></HTML>'
home2 = "hello"
httpMessage = """HTTP/1.0 200 OK\r 
				 Server: ho587\r 
				 Content-Length: 11\r 
				 Content-Type: text/html\r 
				 Connection: Closed\r \n
				 <HTML><HEAD><TITLE>HTTP Homework</TITLE></HEAD> <BODY><H3><CENTER>HTTP Homework</CENTER></H3>This is the main page<P>You can click on <A HREF=”/page2”>page 2</A> or <A HREF=”/page3”>or Page 3</A><P><CENTER>This server has been used XXX times</CENTER></BODY></HTML>
				 """

def client():             # IP layer 3
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    try:
        sock.connect((serverName,serverPort)) #connect requires a tuple
    except OSError:
        print("Sorry, socket couldn't connect");
        return;
    if(sock.sendall(b"GET / HTTP/1.0\r\n\r\n") != None):
        print("Error on sending request!");
        return;
    print("sent successfully, now waiting to receive");
    full_reply = '';
    
    buffer = sock.recv(1024);
    while (buffer): #continue until socket is closed!!
        full_reply +=str(buffer); #convert bytes to UTF16
        buffer = sock.recv(1024);
    header_end = full_reply.find("\\r\\n\\r\\n");
    headers = full_reply[:header_end+8];
    body = full_reply[header_end+8:];
    print(full_reply); 


def host():
	print("Running host...")
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
	sock.bind(("",serverPort))
	sock.listen(1)
	while 1:
		connectionSocket, addr = sock.accept()
		#sentence = sock.recv(1024)
		connectionSocket.sendall(httpMessage.encode('utf-8'))
		connectionSocket.close()

host();
client();