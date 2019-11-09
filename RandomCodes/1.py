class Location():
	def __init__(self, name):
		self.name = name


list_test = [["a","b","c"],["d","e","f"]]

i = 0
while i < len(list_test):
	list_test[i][0] = Location(list_test[i][0])
	list_test[i][2] = Location(list_test[i][2])
	i += 1
print(list_test)