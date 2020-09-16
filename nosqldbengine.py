#!/usr/bin/python3

class NosqlDb:
	'''NosqlDb engine that contains db_main and shemas s1,s2,s3
	and methods for update schemas and store these in db_main.
	 '''
	
	db_main = {'for_1':[],'for_2':[],'for_3':[]}

	def __init__(self):
		self.s1 = {'key1':[],'key2':[]}
		self.s2 = {'field1':[], 'field2':[]}
		self.s3 = {'meta1':[], 'meta2': []}

	#methods here
	def update_s1(self, value1,value2):
		self.s1['key1'].append(value1)
		self.s1['key2'].append(value2)

	def update_main(self):
		if self.s1['key1'] and self.s1['key2']:
			NosqlDb.db_main['for_1'].append(self.s1)


def main():
	print(NosqlDb.__doc__)

if __name__ == '__main__':
	main()