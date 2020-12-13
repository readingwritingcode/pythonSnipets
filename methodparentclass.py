# Calling method on a Parent Class
# call a method in a parent class (or superclass) in place of method that has been overriden in a subclass

class A:
	def spam(self):
		print('A.spam')

class B(A):
	def spam(self):
		print('B.spam')
		super().spam()
# a very common use of super() is in the handling of the __init__() method to make sure that parents are 
# properly initialized:

class A:
	def __init__(self):
		self.x = 0

class B(A):
	def __init__(self):
		super().__init__()
		self.y = 1
# annother common use of super() is in code that overrides any of python's special methods.

class Proxy:
	def __init__(self,obj):
		self._obj = obj

	# Delegate attribute lookup to internal obj
	def __getattr__(self, name):
		return getattr(self._obj, name)
	# Delegate attribute assigment
	def __setattr__(self, name, value):
		if name.startswith('_'):
			super().__setattr__(name,value)
		else:
			setattr(self._obj, name, value)
