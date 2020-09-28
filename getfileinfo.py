#!/usr/bin/python3

'''When we deal with files, we need to extract the filenames in many
scenarios.

'''

import os
from pathlib import Path

#get info 

for py_file in Path().glob('c*.py'):
	print('name with extension:', py_file.name)
	print('name only:',py_file.stem)


#get the extensions 

file_path = Path('clousure.py')
print("file extensions:", file_path-suffix)

#get file size and modification time

current_file_path = Path('file.py')
file_stat = current_file_path.stat()
print("file size in Bytes:", file_stat.st_size)
print("when most recent access:",file_stat.st_atime)
print("when most recent modification:",file_stat.st_mtime)
