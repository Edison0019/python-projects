#this is to sum lists or arrays with the same length

def vector(e1,e2):
	if len(e1) != len(e2):
		return print('vector must have equal length')
	x = len(e1)
	o = []
	for i in range(x):
		o.append(e1[i] + e2[i])
	return o