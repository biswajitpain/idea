import os
import subprocess
def deleteUser(username):
     proc = subprocess.call(['grep' ,'-w', username ,'/etc/passwd'])
     if proc == 0:
         os.system ("sudo userdel " + username)
         return "User %s deleted from the syatem" % username
     else:
         return "User %s is not present in this system" % username
