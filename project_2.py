def remove_vowels(input_string):
    vowels = "aeiou"
    return ''.join(char for char in input_string if char not in vowels)

user_input = input()
result = remove_vowels(user_input)
print( result)


# Function to remove vowels
def rem_vowel(string):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)

# Take user input
string = input("Enter a string: ")
rem_vowel(string)
