#!/usr/bin/python3

class NosqlDb:
	'''NosqlDb schema that contains db_main and shemas s1,s2,s3
	and methods for update schemas with data and store these in db_main.
	 '''
	
	db_main = {'for_s1':[],'for_s2':[],'for_s3':[]}

	def __init__(self):
		self.s1 = {'key1':[],'key2':[]}
		self.s2 = {'field1':[], 'field2':[]}
		self.s3 = {'meta1':[], 'meta2': []}

	#methods here
	def update_s1(self, value1,value2):
		self.s1['key1'].append(value1)
		self.s1['key2'].append(value2)

	def update_s2(self, value1,value2):
		self.s2['field1'].append(value1)
		self.s2['field2'].append(value2)

	def update_s3(self, value1,value2):
		self.s3['meta1'].append(value1)
		self.s3['meta2'].append(value2)

	def update_main(self):

		if self.s1['key1'] and self.s1['key2']:
			NosqlDb.db_main['for_s1'].append(self.s1)
		else:
			NosqlDb.db_main['for_s1'].append('empty')

		if self.s2['field1'] and self.s2['field2']:
			NosqlDb.db_main['for_s2'].append(self.s2)
		else:
			NosqlDb.db_main['for_s2'].append('empty')
		if self.s3['meta1'] and self.s3['meta2']:
			NosqlDb.db_main['for_s3'].append(self.s3)
		else:
			NosqlDb.db_main['for_s3'].append('empty')

	def restart_db_main(self):
		NosqlDb.db_main = {'for_s1':[],'for_s2':[],'for_s3':[]}

def main():
	print(NosqlDb.__doc__)

if __name__ == '__main__':
	main()