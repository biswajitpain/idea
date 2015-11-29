import os
import subprocess
def createUser(name,username,shell,homedir,password,sudo):
     print sudo
     proc = subprocess.call(['grep' ,'-w', username ,'/etc/passwd'])
     if proc == 1:
        if sudo == "True" :
            os.system ("sudo  useradd -p " +password+  " -s " + shell+  " -d " +homedir+username+ " -m " + " -c \""+name+"\" " + username )
            os.system("sudo usermod -a -G sudo " +username )
            return "User %s created in the syatem with sudo prev." % username            
        else:
            os.system ("sudo  useradd -p " +password+  " -s " + shell+  " -d " +homedir+username+ " -m " + " -c \""+name+"\" " + username )         
            return "User %s created in the syatem without sudo prve" % username
     else:
         return "User %s present in this system" % username
