#this module is to split an array into the number of arrays specified in the parameter

var = ['edison','tommy','anthony','josue']

def arraysplit(array,size):
	output = []
	o = []
	index = [x for x in range(0,len(array),len(array) // size)]
	add = range(len(array) // size)
	for x in index:
		o = []
		for y in add:
			o.append(array[x + y])
		output.append(o)
	return output



print(arraysplit(var,2))
