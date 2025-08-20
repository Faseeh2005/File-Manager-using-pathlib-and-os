from pathlib import Path
import os


def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name: ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("what you want to write in the file: ")
                fs.write(data)

            print(F"FILE CREATED SUCCESSFULLY")

        else:
            print("this file already exist")
        
    
    except Exception as err:
        print(f"An error occured as {err}")


def readfile():

    try: 
        readfileandfolder()
        name = input("Which file you wnat to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)

            print("File read successfully")
        else:
            print("File doesnot exist")

    except Exception as err:
        print(f"An error has occured as {err}")


def updatefile():
    try:

        readfileandfolder()
        name = input("Enter which file you want to update: ")
        p =Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing file name")
            print("press 2 for overwriting date in your file")
            print("press 3 for appending data in your file")

            result = int(input("Enter your response: "))

            if result == 1:
                name2 = input("Enter new file name: ")
                p2 =  Path(name2)
                p.rename(p2)
        
            if result == 2:
                with open(p, 'w') as fs:
                    data = input("What you want to write: ")
                    fs.write(data)

            if result == 3:
                with open(p, 'a') as fs:
                    data = input("What you want to add: ")
                    fs.write(" "+data)

    except Exception as err:
        print(f"ann error occured as {err}")


def deletefile():
    try:

        readfileandfolder()
        name = input("Which file you want to delete: ")
        p=Path(name)

        if p.exists() and p.is_file():
            os.remove(p)

            print("file removed")

        else:
            print("no such file exist")

    except Exception as err:
        print(f"Error occured as {err}")



print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("please enter your response: "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()