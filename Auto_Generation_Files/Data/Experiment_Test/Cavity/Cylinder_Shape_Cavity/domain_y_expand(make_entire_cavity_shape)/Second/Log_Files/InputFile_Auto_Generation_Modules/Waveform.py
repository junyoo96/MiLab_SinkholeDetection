from Utility import Utility

class Waveform(Utility):
    def __init__(self,type,max_amplitude,center_frequency,identifier):
        self.type=type
        self.max_amplitude=max_amplitude
        self.center_frequency=center_frequency
        self.identifier=identifier

    def write_textfile(self, textfile):
        text = f"#waveform: {self.type} {self.max_amplitude} {self.center_frequency}e9 {self.identifier}\n"
        textfile.write(text)