import xml.etree.ElementTree as ET
import time
import qualisys_io

a = qualisys_io.qualisys_io("test-cachorro-2","192.168.0.26","password")

a.connect()
time.sleep(1)
p,r = a.get_position_rotation()
print(p,"\n",r)
time.sleep(1)
p,r = a.get_position_rotation()
print(p,"\n",r)
time.sleep(1)
p,r = a.get_position_rotation()
print(p,"\n",r)
time.sleep(1)
p,r = a.get_position_rotation()
print(p,"\n",r)
a.stop() 