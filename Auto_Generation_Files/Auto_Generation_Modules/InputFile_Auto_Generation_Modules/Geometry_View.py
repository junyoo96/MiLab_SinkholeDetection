from Utility import Utility

class Geometry_View(Utility):
    def __init__(self,lower_left_x,lower_left_y,lower_left_z,higher_right_x,higher_right_y,higher_right_z,dx,dy,dz,filename):
        self.lower_left_x = lower_left_x
        self.lower_left_y = lower_left_y
        self.lower_left_z = lower_left_z
        self.higher_right_x = higher_right_x
        self.higher_right_y = higher_right_y
        self.higher_right_z = higher_right_z
        self.dx=dx
        self.dy=dy
        self.dz=dz
        self.filename=filename

    def write_textfile(self, textfile):
        text = f"#geometry_view: {self.lower_left_x} {self.lower_left_y} {self.lower_left_z} {self.higher_right_x} {self.higher_right_y} {self.higher_right_z} {self.dx} {self.dy} {self.dz} {self.filename} n"
        #textfile.write(text)
        textfile.append(text)

        return textfile