#!/usr/bin/python3
from nosqldbengine import NosqlDb

'''Test for NosqlDb'''

#Eschema collection or db_main
db_main = {'for_s1':[], 'for_s2':[],'for_s3':[]}

#Schemas 
s1 = {'key1':[],'key2':[]}
s2 = {'field1':[], 'field2':[]}
s3 = {'meta1':[], 'meta2': []}

expect_db_main = {'for_s1':[{'key1':[0],'key2':[0]},
				            {'key1':[1],'key2':[1]},
				            {'key1':[2],'key2':[2]},
				            {'key1':[3],'key2':[3]},
				            {'key1':[4],'key2':[4]}],
				  'for_s2':[{'field1':[1], 'field2':[1]},
				  			{'field1':[2], 'field2':[2]},
				  			{'field1':[3], 'field2':[3]},
				  			{'field1':[4], 'field2':[4]},
				  			{'field1':[5], 'field2':[5]}],
				  'for_s3':[{'meta1':[2], 'meta2': [2]},
				  			{'meta1':[3], 'meta2': [3]},
				  			{'meta1':[4], 'meta2': [4]},
				  			{'meta1':[5], 'meta2': [5]},
				  			{'meta1':[6], 'meta2': [6]}]}
				  			
def test_nosqldbengine(iter=5,expect_db_main=expect_db_main):
	for i in range(iter):
		_instance = NosqlDb()
		_instance.update_s1(i,i)
		_instance.update_s2(i+1,i+1)
		_instance.update_s3(i+2,i+2)
		_instance.update_main()
		print('hey!')
	print(NosqlDb.db_main)
	print(NosqlDb.db_main == expect_db_main) 

def main():
	return test_nosqldbengine()

if __name__ == '__main__':
	main()