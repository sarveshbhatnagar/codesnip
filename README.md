# Why CodeSnip
Its completely free, open source package which helps you while you code.
It is used to save code snippets in one place and you can access them any time using your terminal/command prompt. 

## Usage

Suppose I have a function which is used to retrieve items from our database and I use that a lot.

function xyz(){
    ...
    ...
}

In such a scenario, I will copy the function and in my terminal

### To save
I will write: codesnip -s "database retrieve items firebase"
This code will save the function you copied. It creates a folder named as database which contains snippets you saved for working on database. 

### If you want to fetch your function
codesnip -f "database retrieve" or codesnip -f "database firebase" or any combination of keys you passed. (NOTE folder name should always be present, in this case its database). This command copies the function to your clipboard, and if multiple functions are found, displays their keys on the terminal to choose from.

### Print existing folders
codesnip -p

### Print all the items in a folder
codesnip -f "database" (KEEP IN MIND, database is folder we created. It can be named anything and you can have any number of folders. This is just used for the sake of example.)

### Export our codesnippets for others
codesnip -e
(Exports to current working directory)

### Import from current working directory
codesnip -ic
(NOTE DO NOT CHANGE NAME OF CODESNIP DATA FILE. IT SHOULD BE OF SAME NAME AS IT WAS WHEN EXPORTED.)

ALSO, when updating package you have to export the data file and then update. After update is complete you need to import the data file again.

### To delete any code snippet in your folder
codesnip -d "database retrieve"