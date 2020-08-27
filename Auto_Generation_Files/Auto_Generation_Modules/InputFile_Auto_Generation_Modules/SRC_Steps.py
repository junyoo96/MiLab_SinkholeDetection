from Utility import Utility

class SRC_Steps(Utility):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def write_textfile(self, textfile):
        text = f"#src_steps: {self.x} {self.y} {self.z}\n"
        #textfile.write(text)
        textfile.append(text)

        return textfile