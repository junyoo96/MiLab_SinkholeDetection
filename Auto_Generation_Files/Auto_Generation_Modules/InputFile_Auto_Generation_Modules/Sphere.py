from Utility import Utility

class Sphere(Utility):
    def __init__(self, x,y,z,radius,material,dielectric_smoothing_activation):
        self.x=x
        self.y=y
        self.z=z
        self.radius=radius
        self.material=material
        self.dielectric_smoothing_activation=dielectric_smoothing_activation

    def write_textfile(self,textfile):
        text=f"#sphere: {self.x} {self.y} {self.z} {self.radius} {self.material} {self.dielectric_smoothing_activation}\n"
        textfile.write(text)
