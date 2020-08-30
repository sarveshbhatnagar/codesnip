from codesnipp import data
import pyperclip

class DataHandler(data.DataStore):
    def __init__(self,object):
        super().__init__()
        self.object = object

    def autofetch(self):
        """
        safely read file from database
        """
        try:
            return self.readFile()
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
            self.saveFile(loadedsnippets)

            print('Code snippet successfully saved.')

        else:
            print('Creating folder {}...'.format(self.object.name))
            loadedsnippets[self.object.name] = [self.object,]

            print('Attempting to save...')
            self.saveFile(loadedsnippets)

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
                self.saveFile(loadedsnippets)
                print('Snippet Deleted!')
            else:
                print('No Snippet found')
            
        else:
            print('Folder not found!')
        
        



