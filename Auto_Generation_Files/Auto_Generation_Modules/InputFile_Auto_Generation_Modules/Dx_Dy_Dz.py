from Utility import Utility

class Dx_Dy_Dz(Utility):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def write_textfile(self, textfile):
        text =f"#dx_dy_dz: {self.x} {self.y} {self.z}\n"
        #textfile.write(text)
        # textfile=textfile+text
        textfile.append(text)
        
        return textfile

