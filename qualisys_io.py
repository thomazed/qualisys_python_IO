import multiprocessing as mt
import lib

class qualisys_io:
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
        print("desconectando")
        self.queue.put("stop")
        self.p1.join()

    
    def get_position_rotation(self):
        try:
            last_position = None
            last_rotation = None
            while not self.queue.empty():
                last_position, last_rotation = self.queue.get()
            if last_position and last_rotation:
                self.posisao = [last_position.x, last_position.y, last_position.z]
                self.rotacao = last_rotation.matrix
                return self.posisao, self.rotacao
            else:
                return None, None
        except Exception as e:
            print(f"Erro ao obter posição e rotação: {e}")
            return None, None