class Folder:
    """
    Folder class to keep all the data organized.
    """
    def __init__(self,name="default",keys=[],snippet=""):
        self.name = name
        self.keys = set(keys)
        self.snippet = snippet

    def getSnippet(self):
        """Gets code snippet"""
        return self.snippet
    
    def getName(self):
        """Gets Name of the folder"""
        return self.name

    def getKeys(self):
        """Gets all the keys in Folder in the form of set"""
        return self.keys
    
    def searchKeys(self,val):
        """Checks if entered value is in keys"""
        return val in self.keys

    def verify(self,name):
        """Checks if the name of folder matches with the passed name"""
        return self.name == name
