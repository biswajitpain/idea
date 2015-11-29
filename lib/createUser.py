import os
import subprocess
def createUser(name,username,shell,homedir,password):
     proc = subprocess.call(['grep' ,'-w', username ,'/etc/passwd'])
     if proc == 1:
         os.system ("useradd -p " +password+  " -s " + shell+  " -d " +homedir+username+ " -m " + " -c \""+name+"\" " + username)
         return "User %s created in the syatem" % username
     else:
         return "User %s present in this system" % username
