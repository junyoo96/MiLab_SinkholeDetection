from Utility import Utility

class Box(Utility):
    def __init__(self,lower_left_x,lower_left_y,lower_left_z,higher_right_x,higher_right_y,higher_right_z,material_identifier,dielectric_smoothing_activation):
        self.lower_left_x=lower_left_x
        self.lower_left_y=lower_left_y
        self.lower_left_z=lower_left_z
        self.higher_right_x=higher_right_x
        self.higher_right_y = higher_right_y
        self.higher_right_z = higher_right_z
        self.material_identifier=material_identifier
        self.dielectric_smoothing_activation=dielectric_smoothing_activation

    def write_textfile(self, textfile):
        text = f"#box: {self.lower_left_x} {self.lower_left_y} {self.lower_left_z} {self.higher_right_x} {self.higher_right_y} {self.higher_right_z} {self.material_identifier} {self.dielectric_smoothing_activation}\n"
        #textfile.write(text)
        textfile.append(text)

        return textfile