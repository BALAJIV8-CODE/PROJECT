# get path 
from pathlib import Path
import os 

# current working directory
#print('Current Working Directory : ' , Path.cwd())

file_name = input('enter the file : ')
print('file name : ' , os.path.basename(file_name))
print('Directory name : ' , os.path.dirname(__file__))