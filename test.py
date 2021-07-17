from ctypes import windll
from PIL import Image
import win32gui
import win32ui


def _find_all_windows(name):
    result = []
    
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == name:
            result.append(hwnd)
    
    win32gui.EnumWindows(winEnumHandler, None)
    return result


window_name = "general - Discord"
windows = _find_all_windows(window_name)
hwnd = windows[0]

left, top, right, bot = win32gui.GetWindowRect(hwnd)
w = right - left
h = bot - top

hwndDC = win32gui.GetWindowDC(hwnd)
mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
saveDC = mfcDC.CreateCompatibleDC()

saveBitMap = win32ui.CreateBitmap()
saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

saveDC.SelectObject(saveBitMap)

# Change the line below depending on whether you want the whole window
# or just the client area.
#result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
print (result)

bmpinfo = saveBitMap.GetInfo()
bmpstr = saveBitMap.GetBitmapBits(True)

im = Image.frombuffer(
    'RGB',
    (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
    bmpstr, 'raw', 'BGRX', 0, 1)

win32gui.DeleteObject(saveBitMap.GetHandle())
saveDC.DeleteDC()
mfcDC.DeleteDC()
win32gui.ReleaseDC(hwnd, hwndDC)

if result == 1:
    #PrintWindow Succeeded
    im.save("test.png")
    
# win32gui.SetForegroundWindow(hwnd)
# bbox = win32gui.GetWindowRect(hwnd)
# img = ImageGrab.grab(bbox)
# img.show()
# time.sleep(2)
print(win32gui.GetForegroundWindow())
notepad_id = 264006

# print(win32gui.isWindowVisible(264006))
# print(win32gui.Get)
