from streaming import *
import threading

def find_all_windows():
    result = []
    nameapp = []
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and not win32gui.GetWindowText(hwnd) == "" :
            result.append(hwnd)
            nameapp.append(win32gui.GetWindowText(hwnd))
    
    win32gui.EnumWindows(winEnumHandler, None)
    return result, nameapp

def select_app():
    ids, names = find_all_windows()
    for i in range(len(ids)):
        print("{} - {} - {}".format(i, ids[i], names[i]))
        
    select = int(input("select app: "))
    return ids[select], names[select]


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
# radmin_ip = '26.158.223.89'
ip_radmin = ''
with open("config.txt", 'r', encoding='utf-8') as r:
    ip_radmin = r.readline().replace("\n","")
    print(ip_radmin)
    x_res = int(r.readline().replace("\n",""))
    y_res = int(r.readline().replace("\n",""))
    r.close()
# sender = ScreenShareClient(local_ip, 9999, 1920, 1080)
sender = ScreenShareClient(ip_radmin, 9999, x_res, y_res)
# app, name = select_app()
# sender = AppShareClient(local_ip, 9999, name,1600, 900)
# sender = AppShareClient(local_ip, 9999, name)



t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != 'STOP':
    continue

sender.start_stream()