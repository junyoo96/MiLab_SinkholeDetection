from Utility import Utility

class Time_Window(Utility):
    def __init__(self,time_window):
        self.time_window=time_window

    def write_textfile(self, textfile):
        text = f"#time_window: {self.time_window}\n"
        textfile.write(text)