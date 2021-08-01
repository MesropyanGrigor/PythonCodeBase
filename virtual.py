class A:
	def __init__(self):
		self.__a = 12
		self.b = 33
	def __getattribute__(self, nn):
		#print(nn)
		if nn.startswith(f"_{super(A, self).__getattribute__('__class__').__name__}"):
			raise AttributeError("Is not allowed to access private member")
		return super(A, self).__getattribute__(nn)

	
a = A()
print(dir(a))
print(a.b)
print(a._A__a)
