# import os

# filePath = "Python/tester.txt"

# if os.path.exists(filePath): 
#   print("The location exists")
# else: 
#   print("The location doesn't exists")

#USING PATHLIB(MODERN WAY)

from pathlib import *

path = Path("Python/tempFile.txt") #Here path ios a Path object, not only a string

#cheecking if file exists
print(f"Checking if file exists: {path.exists()}")

#check if it's a file or folder
print(f"Check if it's a file: {path.is_file()}")
print(f"Check if it's a folder: {path.is_dir()}")

#find current working directory(cwd)
print(f"Current working directory: {Path.cwd()}")

#find the location of script or just the folder in which its present
print(f"Script location: {Path(__file__)}")
print(f"Folder containing the script: {Path(__file__).parent}")

#Making file path
current_folder = Path(__file__).parent
file_path = current_folder/"tester.txt" #'/' is used to join file path
print(f"Made file path: {file_path}")
print()

#Opening a file
with path.open("r") as file:
  print(f"Opened file contents:\n{file.read()}")
print()

#Read a file directly
print(f"Read file directly:\n{path.read_text()}")
print()

#Write a file directly, if file doesn't exist it will create that file
path.write_text("NEW TEXT INSERTED!!!")  

#Create folder
# folder = Path("NOtes")
# folder.mkdir()

#Delete file or folder
# Path("filename.extension").unlink()
# Path("Notes").rmdir()

#Rename a file
# oldName = Path("Python/tester.txt")
# oldName.rename("Python/tempFile.txt")

#Get file name or extension
_path = Path("Python/property.py")
print(_path.name) #File name with extension
print(_path.stem) #File name without extension
print(_path.suffix) #File extension
