from streaming import *
import threading


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
radmin_ip = ''

receiver = StreamingServer(local_ip, 9999)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    continue
    
receiver.stop_server()