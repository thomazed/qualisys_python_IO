import xml.etree.ElementTree as ET
import time
from qualisys_tools import qualisys_io

a = qualisys_io("lego","192.168.0.26","password")

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