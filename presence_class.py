from pypresence import Presence
import time


class Discord:
    def __init__(self):
        self.idclient = '724944148238565416'

        self.details = "default"
        self.state = "Développée par BeeWildz#0101"
        self.RPC = Presence(self.idclient)
        self.L_image=""
        self.S_image=""

    def start(self):
        self.RPC.connect()
        print("Connect to the app '"+self.idclient+ "'" )
        self.RPC.update(state=self.state,
                         details=self.details , large_image="default.png") # Set the presence


        print("Default update")

