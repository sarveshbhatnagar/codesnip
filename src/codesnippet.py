import argparse
from codesnipp import datahandler, folder
import pyperclip


def main():
    parser = argparse.ArgumentParser(description="This Program lets you save and retrieve code snippets. To save a snippet first copy a code snippet and run -s command. To fetch snippet, use -f command and it will be copied to clipboard!")
    parser.add_argument('-s','--save',type=str,help="Saves your code snippet from clipboard along with the keys you pass. e.g. codesnippet -s 'Flutter database retrieve'")
    parser.add_argument('-f','--fetch',type=str,help="Fetches records from the database. e.g. codesnippet -f 'flutter database' or 'flutter retrieve database'")
    parser.add_argument('-d','--deleterecord',type=str,help="Delete's a records from the database. e.g. codesnippet -d 'flutter database' or 'flutter retrieve database'")
    args = parser.parse_args()

    if(args.save):
        lis = args.save.split(' ')
        #Create folder object
        folderobj = folder.Folder(name=lis[0],keys=lis[1:],snippet=pyperclip.paste())
        #Add that folder object to list in dictionary we need to get dictionary.
        datahandler.DataHandler(object=folderobj).handleSave()
        
    elif args.fetch:
        lis = args.fetch.split(' ')
        datahandler.DataHandler(folder.Folder()).handleFetch(lis[0],lis[1:])
        #Data handler works but I need to consider all the keys.
    elif args.deleterecord:
        lis = args.deleterecord.split(' ')
        datahandler.DataHandler(folder.Folder()).handleDelete(lis[0],lis[1:])
    else:
        print("""\
Please use either -s command to save code snippet or -f command to fetch code snippet
Use -d command to delete a code snippet from saved snippets.

Usage: 
    codesnippet -s '[FOLDER_NAME [KEY STRING]'
    codesnippet -f '[FOLDER_NAME] [ANY KEY]'
    codesnippet -d '[FOLDER_NAME [ANY KEY]'
        
e.g. 
    codesnippet -s 'flutter save to database'
    codesnippet -f 'flutter save database' or 'flutter database'
    codesnippet -d 'flutter save database' or 'flutter database'
""")


