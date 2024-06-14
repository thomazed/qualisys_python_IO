import asyncio  
import xml.etree.ElementTree as ET
import pkg_resources
import multiprocessing as mt
import time

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
        self.queue = mt.Queue()
        self.p1 = mt.Process(target=lib.run,args=(self.queue,self._6DOF_Name,self.IP,self.Password))
        
        
    def connect(self):
        print("conectando")
        self.p1.start()
        
            

    def stop(self):
        print("oi")
        self.queue.put("stop")
        self.p1.join()