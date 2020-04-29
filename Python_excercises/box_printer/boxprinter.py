def boxprint(symbol,width, height):
	if len(symbol) != 1:
		raise Exception('Symbol must be a single character string')
	if width <= 2:
		raise Exception('Width must be grater than 2')
	if height <= 2:
		raise Exception('Height must be grater than 2')
	print(symbol * width)
	for i in range(height - 2):
		print(symbol + (' ' * (width -2)) + symbol)
	print(symbol * width)