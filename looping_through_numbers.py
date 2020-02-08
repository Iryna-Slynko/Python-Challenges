#The loop function takes in 3 parameters: the starting point, the stopping point, and the increment step. 
#When the starting point is greater than the stopping point, it forces the steps to be negative. 
#When, instead, the starting point is less than the stopping point, it forces the step to be positive. 
#Also, if the step is 0, it changes to 1 or -1.
#The result is returned as a one-line, space-separated string of numbers. 

def loop(start, stop, step):
	return_string = ""
	if step == 0:
		step=1
	if start>stop:
		step = abs(step) * -1
	else:
		step = abs(step)
	for count in range(start, stop, step):
		return_string += str(count) + " "
	return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
print(loop(1,1,1)) # Should be empty
