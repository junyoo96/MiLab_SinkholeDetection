from Utility import Utility

class Material(Utility):
    def __init__(self,relative_permittivity, conductivity, relative_permeability,magnetic_loss,identifier):
        self.relative_permittivity=relative_permittivity
        self.conductivity=conductivity
        self.relative_permeability=relative_permeability
        self.magnetic_loss=magnetic_loss
        self.identifier=identifier

    def write_textfile(self, textfile):
        text = f"#material: {self.relative_permittivity} {self.conductivity} {self.relative_permeability} {self.magnetic_loss} {self.identifier}\n"
        #textfile.write(text)
        textfile.append(text)
        
        return textfile
        