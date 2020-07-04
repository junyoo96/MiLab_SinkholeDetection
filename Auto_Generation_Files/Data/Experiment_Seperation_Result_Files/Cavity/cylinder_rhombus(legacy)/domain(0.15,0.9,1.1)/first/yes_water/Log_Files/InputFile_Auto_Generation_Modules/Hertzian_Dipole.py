from Utility import Utility

class Hertzian_Dipole(Utility):
    def __init__(self,source_polarisation,source_x,source_y,source_z,source_identifier):
        self.source_polarisation=source_polarisation
        self.source_x=source_x
        self.source_y=source_y
        self.source_z=source_z
        self.source_identifier=source_identifier

    def write_textfile(self, textfile):
        text =f"#hertzian_dipole: {self.source_polarisation} {self.source_x} {self.source_y} {self.source_z} {self.source_identifier}\n"
        textfile.write(text)