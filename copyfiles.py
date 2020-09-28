#!/usr/bin/python3

'''to copy files, we can take advantage of the functionalities
   avaible in the shutil module, which is another useful module
   for file operations in the standar library'''

  import shutil
  from pathlib

  source_file = "target_folder/file.ext"
  target_file = "file2.ext"
  target_file_path = Path(target_file)
  print("Before copying, file exist:", target_file_path.exist())
  shutil.copy(source_file,target_file)
  print("After copying, file exist:", target_file_path.exist())