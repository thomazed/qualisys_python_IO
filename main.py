import asyncio  
import xml.etree.ElementTree as ET
import pkg_resources

import qtm_rt
import lib

class Main:
    def __init__(self,_6DOF_Name,IP,Password):
        self._6DOF_Name = _6DOF_Name
        self.IP = IP
        self.Password = Password
        self.isRunning = True
        self.posisao = [0,0,0]
        self.rotacao = [0,0,0,0,0,0]
        
        
    def connect(self):
        asyncio.get_event_loop().run_until_complete(lib.main())