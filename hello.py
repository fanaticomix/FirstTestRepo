# Function to reverse a string
def reverse(string):
	string = string[::-1]
	return string

def isPalindrome(string):
	reversedString = reverse(string) 
	if string == reversedString:
		return True
	return False


word = "reinier"

if isPalindrome(word):
	print("Es palindrome")
else:
	print( "No es palindrome")