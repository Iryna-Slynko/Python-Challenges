#This function prints out a multiplication table. 
#Each number is the result of multiplying the first number of its row by the number at the top of its column.
#Assignment from Automation with Python course by Google at coursera.org

def multiplication_table(start, stop):
	for x in range(start,stop+1):
		for y in range(start, stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
