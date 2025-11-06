import subprocess   

def OpenCMDMessage():
    subprocess.Popen("start cmd /k python c:/Users/santo/Documents/ReturnToForm/message.py", shell=True)

if __name__ == '__main__':
    OpenCMDMessage()