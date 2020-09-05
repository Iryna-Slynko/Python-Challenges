'''def is_palindrome(r_phrase):
    j=0
    for i in range(len(r_phrase)-1,len(r_phrase)//2,-1):
        if r_phrase[j]!= r_phrase[i]:
            return False
        j+=1
    return True
print(is_palindrome(r_phrase))'''

def is_palindrome(input_string):

	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for char in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if char!=" ":
			new_string = new_string + char
			reverse_string = char + reverse_string
	# Compare the strings
	if new_string.lower()==reverse_string.lower():
		return True
	return False

print(is_palindrome("Never Odd or Even")) # True
print(is_palindrome("abc")) # False
print(is_palindrome("kayak")) # True
