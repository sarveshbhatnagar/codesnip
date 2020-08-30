import codesnipp.folder
import pickle

class DataStore:
    """This class will be responsible for storing, retrieving and other operations on data"""
    filename = 'code_snippet_datastorage_file'

    def __init__(self,):
        pass

    def saveFile(self,obj):
        with open(self.filename,'wb') as f:
            pickle.dump(obj, f)

    def readFile(self):
        with open(self.filename,'rb') as f:
            x = pickle.loads(f.read())
        return x
