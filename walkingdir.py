#!/usr/bin/python3

'''reusalble directory walking module'''
import os
import sys

class diskwalk(object):
	"""reudsable directory walking module.
		input= path variable: path to directory.
		methods = path to files in directory; files in a directory;
				  directories in a list of directories
	"""
	def __init__(self, path):
		self.path = path

	def enumeratePaths(self):
		'''return th path to all the files in a directory 
		   as a list.
		'''
		path_list = []
		for root, dirs, files in os.walk(self.path):
			for file in files:
				path_list.append(os.path.join(root,file))
		return path_list

	def enumerateFiles(self):
		list_files = []
		for root,dirs,files in os.walk(self.path):
			for file in files:
				list_files.append(file)
		return list_files

	def enumerateDir(self):
		list_dir = []
		for root, dirs, files in os.walk(self.path):
			for dir in dirs:
				list_dir.append(dir)
		return list_dir

def main():
	_dir = diskwalk(sys.argv[1])

	_dir.enumeratePaths()
	print('task one done!')

	_dir.enumerateFiles()
	print('task two done!')

	_dir.enumerateDir()
	print('task tree done!')

	print(_dir.enumeratePaths(), _dir.enumerateFiles(), _dir.enumerateDir())

if __name__ == '__main__':
	main()