from Utility import Utility

class Cylinder(Utility):
    def __init__(self, lower_x, lower_y, lower_z, higher_x, higher_y, higher_z,radius, material_identifier, dielectric_smoothing_activation):
        self.lower_x=lower_x
        self.lower_y=lower_y
        self.lower_z=lower_z
        self.higher_x=higher_x
        self.higher_y = higher_y
        self.higher_z = higher_z
        self.radius=radius
        self.material_identifier=material_identifier
        self.dielectric_smoothing_activation=dielectric_smoothing_activation

    def write_textfile(self, textfile):
        text = f"#cylinder: {self.lower_x} {self.lower_y} {self.lower_z} {self.higher_x} {self.higher_y} {self.higher_z} {self.radius} {self.material_identifier} {self.dielectric_smoothing_activation}\n"
        textfile.write(text)