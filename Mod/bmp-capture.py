import win32gui
import win32ui
import win32con
from ctypes import windll

hdesktop = win32gui.GetDesktopWindow()

screen = windll.user32
screen.SetProcessDPIAware()
width=screen.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height=screen.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)

left = screen.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = screen.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

desktop_dc = win32gui.GetWindowDC(hdesktop)

img_dc = win32ui.CreateDCFromHandle(desktop_dc)

mem_dc = img_dc.CreateCompatibleDC()

screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width,height)
mem_dc.SelectObject(screenshot)

mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

screenshot.SaveBitmapFile(mem_dc, 'screenshot.bmp')

mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())