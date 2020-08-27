from Utility import Utility

class Hertzian_Dipole(Utility):
    def __init__(self,source_polarisation,source_x,source_y,source_z,source_identifier):
        self.source_polarisation=source_polarisation
        self.source_x=source_x
        self.source_y=source_y
        self.source_z=source_z
        self.source_identifier=source_identifier

    def write_textfile(self,source_x_list):
        hertzian_dipole_list=[]
        for i in range(len(source_x_list)):
            text =f"#hertzian_dipole: {self.source_polarisation} {source_x_list[i]} {self.source_y} {self.source_z} {self.source_identifier}\n"
            hertzian_dipole_list.append(text)
        
        return hertzian_dipole_list