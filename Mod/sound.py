import win32api


FREQUENCY=[392,392,440,392,523,494,392,392,440,392,587,523,392,392,784,659,523,494,440,689,689,523,587,523]
DELAY = [375,125,500,500,500,1000,375,125,500,500,500,1000,375,125,500,500,500,500,1000,375,125,500,500,500,1000]
for i in range(0,24):
	win32api.Beep(FREQUENCY[i],DELAY[i])
	
win32api.MessageBox(hwnd, message , title , style , language )
#hwnd:父窗口的句柄,一般为0
#message:消息
#title:标题
#style和language均有默认值，可以不填

win32api.ShellExecute(hwnd, op , file , params , dir , bShow )
#打开某个文件，file填打开文件的目录
#win32api.ShellExecute(0,'open',r'C:\Users\tqb\Desktop\MCC\NothingInTheWorld.mp3','','',1)