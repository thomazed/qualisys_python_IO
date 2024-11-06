import multiprocessing as mt


import asyncio  
import xml.etree.ElementTree as ET
import pkg_resources
import qtm_rt

QTM_FILE = pkg_resources.resource_filename("qtm_rt", "data/Demo.qtm")

def run(queue,_6DOF_Name,IP,Password):
    asyncio.get_event_loop().run_until_complete(main(queue,_6DOF_Name,IP,Password))


def create_body_index(xml_string):
    """ Extract a name to index dictionary from 6dof settings xml """
    xml = ET.fromstring(xml_string)

    body_to_index = {}
    for index, body in enumerate(xml.findall("*/Body/Name")):
        body_to_index[body.text.strip()] = index

    return body_to_index

def body_enabled_count(xml_string):
    xml = ET.fromstring(xml_string)
    return sum(enabled.text == "true" for enabled in xml.findall("*/Body/Enabled"))

async def main(queue,_6DOF_Name,IP,Password):

    # Connect to qtm
    connection = await qtm_rt.connect(IP)

    # Connection failed?
    if connection is None:
        print("Failed to connect")
        return

    # Take control of qtm, context manager will automatically release control after scope end
    async with qtm_rt.TakeControl(connection, Password):

        realtime = True

        if realtime:
            # Start new realtime
            await connection.new()
        else:
            # Load qtm file
            await connection.load(QTM_FILE)

            # start rtfromfile
            await connection.start(rtfromfile=True)

    # Get 6dof settings from qtm
    xml_string = await connection.get_parameters(parameters=["6d"])
    body_index = create_body_index(xml_string)

    print("{} of {} 6DoF bodies enabled".format(body_enabled_count(xml_string), len(body_index)))

    wanted_body = _6DOF_Name

    def on_packet(packet):
        info, bodies = packet.get_6d()

        #print("Framenumber: {} - Body count: {}".format(packet.framenumber, info.body_count))

        if wanted_body is not None and wanted_body in body_index:
            # Extract one specific body
            wanted_index = body_index[wanted_body]
            position, rotation = bodies[wanted_index]
            queue.put((position,rotation))

            
        else:
            # Print all bodies
            for position, rotation in bodies:
                print("ERROR: não pode achar corpo rigido")

    # Start streaming frames
    await connection.stream_frames(components=["6d"], on_packet=on_packet)

    while(True):
        await asyncio.sleep(1)
        msg = await asyncio.to_thread(queue.get)
        if msg == "stop":
            break




class qualisys_io:
    def __init__(self,_6DOF_Name,IP,Password):
        self._6DOF_Name = _6DOF_Name
        self.IP = IP
        self.Password = Password
        self.isRunning = True
        self.posisao = [0,0,0]
        self.rotacao = [0,0,0,0,0,0]
        self.queue = mt.Queue()
        self.p1 = mt.Process(target=run,args=(self.queue,self._6DOF_Name,self.IP,self.Password))
        
        
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