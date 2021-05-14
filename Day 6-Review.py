num_test_cases = int(input())

for i in range (num_test_cases):
    test_string = input()
    even_indexed_characters = ''
    odd_indexed_characters = ''
    
    for j in range(len(test_string)):
        if j%2 == 0:
            even_indexed_characters += test_string[j]
        else:
            odd_indexed_characters += test_string[j]
            
    print('{} {}'.format(even_indexed_characters,odd_indexed_characters))   
	
	
	
	
# First we have to take the input of the number of Strings 

NumberOfStrings = int(input())

# for loop from 0 to the length of the String

for i in range(0, NumberOfStrings):
    
    # Taking input from the User 
    
    string = input()
    
    # The below line has two parts 1. string[::2] & 2. string[1::2].
    # General format is [start:stop:step].
    # 1. string[::2] basically means that start from 0 to the end of the String skipping 2 characters hence taking all even strings 
    # 2. string[1::2] same as the above but we start from 1 and not 0 
    
    print(string[::2],string[1::2])     