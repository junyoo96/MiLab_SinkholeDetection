from Utility import Utility

class Rx(Utility):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def write_textfile(self, textfile):
        text = f"#rx: {self.x} {self.y} {self.z}\n"
        textfile.write(text)