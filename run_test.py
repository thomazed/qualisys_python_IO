import asyncio  
import xml.etree.ElementTree as ET
import pkg_resources
import time

import qtm_rt
import main

a = main.Main("test-cachorro-2","192.168.0.26","password")

a.connect()
time.sleep(10)
a.stop()