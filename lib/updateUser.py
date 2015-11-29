import os
import subprocess
def updateUser(name,username,shell,homedir,password):
     proc = subprocess.call(['grep' ,'-w', username ,'/etc/passwd'])
     if proc == 0:
         os.system ("sudo usermod -p " +password+  " -s " + shell+  " -d " +homedir+username+ " -m " + " -c \""+name+"\" " + username)
         return "User %s updated in the syatem" % username
     else:
         return "User %s is not  present in this system" % username
