from streaming import *
import threading

ip_radmin = ''
with open("config.txt", 'r', encoding='utf-8') as r:
    ip_radmin_myself = r.readline().replace("\n","")
    r.close()

# hostname = socket.gethostname()
# local_ip = socket.gethostbyname(hostname)
# radmin_ip = '26.158.223.89'

receiver = StreamingServer(ip_radmin_myself, 9999)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    continue
    
receiver.stop_server()