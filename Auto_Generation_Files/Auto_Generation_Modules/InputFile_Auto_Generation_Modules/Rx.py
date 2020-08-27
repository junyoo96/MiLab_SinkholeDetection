from Utility import Utility

class Rx(Utility):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def write_textfile(self, source_x_list):
        rx_list=[]
        for i in range(len(source_x_list)):
            text = f"#rx: {source_x_list[i]} {self.y} {self.z}\n"
            rx_list.append(text)
        
        return rx_list
