import os

def start():
	os.chdir('C:\\Users\\NaiTuTreaba\\Desktop\\minecraft')
	return os.system('start server.jar')

def stop():
	return os.system("taskkill /im javaw.exe")

def get_minecraft():
	return 'https://mega.nz/file/zChiiCrL#rmZo8XydBvDOyTIvGNSAxeW7aTZZTKKFsAE3sjcCIrk'
	