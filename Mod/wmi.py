from win32com.client import GetObject

wmi = GetObject('winmgmts:\\\\.\\root\\SecurityCenter2').InstancesOf('AntiVirusProduct')
	
for obj in wmi:
	if obj.displayName != None:
		print("displayName:" + str(obj.displayName))
	if obj.pathToSignedProductExe != None:
		print("ProductExe:" + str(obj.pathToSignedProductExe))