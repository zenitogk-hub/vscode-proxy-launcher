import subprocess

command = 'code --proxy-server="http://192.168.15.1:8090"'
subprocess.Popen(command, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
