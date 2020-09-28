#/usr/bin/python3

'''Move files in python.
In python these jobs can be done really easily. To move a file,
you simply rename the file by replacing its old directory with its
target directory.'''

import os
from pathlib import Path 

target_folder = Path("target_folder")
target_folder.mkdir(parents=True, exist_ok=True) # i have a dude here
source_folder = Path('.')

txt_files = source_folder.glob('*.txt')
for txt_file in txt_files: 
	file_name = txt_file.name 
	target_path = target_folder.joinpath(file_name)
	print("Moving:"  file_name)
	print(target_path.exist()) #this raise false
	txt_file.rename(target_path)
	print(target_path.exist()) #this raise true, because file has been move rename
