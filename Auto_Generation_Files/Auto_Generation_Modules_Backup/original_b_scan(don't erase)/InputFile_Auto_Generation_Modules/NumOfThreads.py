from Utility import Utility

class NumOfThreads(Utility):
    def __init__(self,numOfThreads):
        self.numOfThreads=numOfThreads

    def write_textfile(self,textfile):
        text = f"#num_threads: {self.numOfThreads}\n"
        textfile.write(text)
