import argparse
import pyperclip,pickle
import os

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


class DataHandler:
    # path = os.path.join(data.__file__,'newstoredfile')
    def __init__(self,objectp,fpath):
        self.object = objectp
        self.fpath = fpath

    

    def saveFile(self,obj,p):
        """Saves file to the given path safely"""
        with open(p,'wb') as f:
            pickle.dump(obj, f)

    def readFile(self,p):
        """Reads file from the given path safely"""
        with open(p,'rb') as f:
            x = pickle.loads(f.read())
        return x

    def autofetch(self):
        """
        safely read file from database, returns a dict.
        """
        try:
            return self.readFile(self.fpath)
        except Exception:
            return dict()
    
    def handleSave(self):
        """
        fetches data and checks if folder is there. Adds key accordingly.
        """

        print('Loading Snippets...')
        loadedsnippets = self.autofetch()

        if self.object.name in loadedsnippets:

            print('Folder {} Already Created...'.format(self.object.name))
            loadedsnippets[self.object.name].append(self.object)

            print('Attempting to save...')
            self.saveFile(loadedsnippets,self.fpath)

            print('Code snippet successfully saved.')

        else:
            print('Creating folder {}...'.format(self.object.name))
            loadedsnippets[self.object.name] = [self.object,]

            print('Attempting to save...')
            self.saveFile(loadedsnippets,self.fpath)

            print('Code snippet successfully saved.')






    def handleFetch(self,folder,keys):
        """Code to handle fetching of snippets using folder and keys"""

        print('Loading Snippets...')
        loadedsnippets = self.autofetch()

        if folder in loadedsnippets:
            items = loadedsnippets[folder]
            lis = []
            maxval = 0
            for item in items:
                val = len(item.getKeys() & set(keys))
                if(val == maxval):
                    lis.append(item)
                elif(val > maxval):
                    maxval = val
                    lis.clear()
                    lis.append(item)
            if(len(lis) > 1):
                #Multiple Results.
                self.handleMultipleList(lis,'fetch')
            elif(len(lis) == 1):
                print('Copying Snippet to Clipboard...')
                pyperclip.copy(lis[0].getSnippet())
                print('Copied!')
            else:
                print('Snippets not found...')
            
        else:
            print('Folder not found!')




    def handleMultipleList(self,lis,operation,):
        """Used when there are multiple results"""
        print('\nSelect your Snippet Key\n')
        for ind,it in enumerate(lis):
            print(ind," ",it.keys)
        
        if(operation == 'fetch'):
            while(True):
                try:
                    selection = int(input('Enter your selection (e.g. 0) '))
                    print('Fetching your Snippet...')
                    pyperclip.copy(lis[selection].getSnippet())
                    print('Snippet copied!')
                    break
                except:
                    print('Err... Selection invalid! Try again.')
        elif(operation == 'deleterecord'):
            while(True):
                try:
                    selection = int(input('Enter your selection (e.g. 0) '))
                    print('Deleting your Snippet...')
                    delselection = lis.pop(selection)
                    return delselection
                except:
                    print('Err... Selection invalid! Try again.')





    def handleDelete(self,folder,keys):
        print('Loading Snippets...')
        loadedsnippets = self.autofetch()

        if folder in loadedsnippets:
            items = loadedsnippets[folder]
            lis = []
            maxval = 0
            for item in items:
                val = len(item.getKeys() & set(keys))
                if(val > 0):
                    lis.append(item)
            if(len(lis) > 0):
                delselection = self.handleMultipleList(lis,'deleterecord')
                items.remove(delselection)
                loadedsnippets[folder] = items
                self.saveFile(loadedsnippets,self.fpath)
                print('Snippet Deleted!')
            else:
                print('No Snippet found')

        else:
            print('Folder not found!')

    def handlePrint(self):
        loadedsnippets = self.autofetch()
        if len(loadedsnippets) == 0:
            print('There are no folders available to display...')
        for i,k in enumerate(loadedsnippets.keys()):
            print(i,'. ',k)

    def handleImport(self,importpath):
        print('Trying to import...')
        try:
            loadsnippet = self.readFile(importpath)
            internalsnippets =  self.autofetch()
            # Two dictionaries, work with them.
            # fdic = {'a':[1,],'b':[2,],'c':[3,]}
            # sdic = {'a':[4,],'d':[2,],'e':[3,]}
            commonkey = set(loadsnippet.keys()) & set(internalsnippets.keys())
            if(len(commonkey) == 0):
                # update internalsnippets
                internalsnippets.update(loadsnippet)
            else:
                #TODO check if it can be optimized.
                for k in commonkey:
                    internalsnippets[k] = internalsnippets[k] + loadsnippet[k]
                for val in loadsnippet.keys():
                    if(val not in k):
                        internalsnippets[val] = loadsnippet[val]
            self.saveFile(internalsnippets,self.fpath)
            print('Import successful.')
        except:
            print('There was an error loading file. Use -ic to import from current directory.')
            return




def main():
    parser = argparse.ArgumentParser(description="This Program lets you save and retrieve code snippets. To save a snippet first copy a code snippet and run -s command. To fetch snippet, use -f command and it will be copied to clipboard!")
    parser.add_argument('-s','--save',type=str,help="Saves your code snippet from clipboard along with the keys you pass. e.g. codesnippet -s 'Flutter database retrieve'")
    parser.add_argument('-f','--fetch',type=str,help="Fetches records from the database. e.g. codesnippet -f 'flutter database' or 'flutter retrieve database'")
    parser.add_argument('-d','--deleterecord',type=str,help="Delete's a records from the database. e.g. codesnippet -d 'flutter database' or 'flutter retrieve database'")
    parser.add_argument('-p','--printfolders',help='Used to print all the available folders',action='store_true',default=False)
    #TODO add import
    parser.add_argument('-i','--importfile',type=str,help="Imports the datafilestore_codesnip file from the passed location. (Appends instead of resetting)")
    parser.add_argument('-ic','--importcwd',help="Imports datafile from current working directory.",action='store_true',default=False)
    parser.add_argument('-e','--exportfile',help="Exports file at current working directory for you to backup and share.",action='store_true',default=False)
    args = parser.parse_args()
    myfilepath = os.path.join(os.path.dirname(__file__),'datafilestore_codesnip')
    dhobj = DataHandler(Folder(),myfilepath)
    if(args.save):
        lis = args.save.split(' ')
        #Create folder object
        folderobj = Folder(name=lis[0],keys=lis[1:],snippet=pyperclip.paste())
        #Add that folder object to list in dictionary we need to get dictionary.
        DataHandler(objectp=folderobj,fpath=myfilepath).handleSave()
        
    elif args.fetch:
        lis = args.fetch.split(' ')
        dhobj.handleFetch(lis[0],lis[1:])
        #Data handler works but I need to consider all the keys.
    elif args.deleterecord:
        lis = args.deleterecord.split(' ')
        dhobj.handleDelete(lis[0],lis[1:])
    elif args.printfolders:
        dhobj.handlePrint()
    elif args.importfile:
        print('Will be implemented soon... use -ic for current directory.')
    elif args.importcwd:
        DataHandler(Folder(),os.path.join(os.path.dirname(__file__),'datafilestore_codesnip')).handleImport(os.path.join(os.getcwd(),'datafilestore_codesnip'))
    elif args.exportfile:
        filepath = os.getcwd()
        fetchfile = dhobj.autofetch()
        print('Exporting to {0}...'.format(filepath))
        dhobj.saveFile(fetchfile,os.path.join(filepath,'datafilestore_codesnip'))
        print('Export successful.')

        #TODO Create save data in datahandler
    else:
        print("""\
NOTE: Before you update, remember to export the data and after update, import the data.
Please use either -s command to save code snippet or -f command to fetch code snippet
Use -d command to delete a code snippet from saved snippets. 
Use -p command to print all the available folders.
Use -e to export to current working directory.
Use -i to import from specific path
Use -ic to import from current directory. filename should be datafilestore_codesnip.

Usage: 
    codesnip -s '[FOLDER_NAME [KEY STRING]'
    codesnip -f '[FOLDER_NAME] [ANY KEY]'
    codesnip -d '[FOLDER_NAME [ANY KEY]'
    codesnip -p
    codesnip -e
    codesnip -i 'PATH TO CODESNIP DATA'
    codesnip -ic
        
e.g. 
    codesnippet -s 'flutter save to database'
    codesnippet -f 'flutter save database' or 'flutter database'
    codesnippet -d 'flutter save database' or 'flutter database'
""")


