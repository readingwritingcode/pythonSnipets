#!/usr/bin/python3

#read file

with open('path/to/file.ext','r') as file:
	content = file.read()

#read line by line:
with open('path/to/file.ext','r') as file:
	for num,line in enumerate(file):
		print(num,"line is:",line)

#write files
with open('path/to/save/file.ext','w') as file:
	file.write('hola mundo')

#write file from multiple lineas of text data
with open('path/to/save/file.ext','a') as file:
	for line in list_of_lines:
		file.write('\n'+line)
