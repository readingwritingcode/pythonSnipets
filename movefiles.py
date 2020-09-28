#/usr/bin/python3

'''Move files in python.
In python these jobs can be done really easily. To move a file,
you simply rename the file by replacing its old directory with its
target directory.'''

import os
import sys
from pathlib import Path 

def move_files(target_folder,source_folder, file, file_ext):
	target_folder = Path(target_folder)
	target_folder.mkdir(parents=True, exist_ok=True) # i have a dude here
	source_folder = Path(source_folder)

	txt_files = source_folder.glob('*.' + file_ext)
	for txt_file in txt_files: 
		file_name = txt_file.name 
		target_path = target_folder.joinpath(file_name)
		txt_file.rename(target_path)
	return os.listdir(target_folder)

def main():
	move_files(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
	main()