from Utility import Utility

class Title(Utility):
    def __init__(self,title):
        self.title=title

    def write_textfile(self,textfile):
        text = f"#title: {self.title}\n"
        textfile.append(text)

        return textfile
        
