import os
import subprocess
def updateUser(name,username,shell,homedir,password,sudo):
     proc = subprocess.call(['grep' ,'-w', username ,'/etc/passwd'])
     if proc == 0:
	 if sudo == "True":
             os.system ("sudo usermod -p " +password+  " -s " + shell+  " -d " +homedir+username+ " -m " + " -c \""+name+"\" " + username+ "-aG sudo")
             return "User %s updated in the syatem with sudo prev" % username
         else:
             os.system ("sudo usermod -p " +password+  " -s " + shell+  " -d " +homedir+username+ " -m " + " -c \""+name+"\" " + username )
             os.system ("sudo deluser "+ username+ " sudo")
             return "User %s updated in the system without sudo prev" % username
     else:
         return "User %s is not  present in this system" % username
