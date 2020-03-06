def exponentiate(x, y):

"""
Takes x and raises it to the value of y.
"""	
	return	(x ** y)

def raise_to_fourth_power(y):

""" 
Takes the value Z and runs 
it through the exponentiate function 
with predetermined value of 4 as the power.
"""	
	return exponentiate(y, 4)	

square = lambda y: exponentiate(y, 2)

cube = lambda y: exponentiate(y, 3)

print((square(2)))
print((cube(2)))
print((raise_to_fourth_power(2)))