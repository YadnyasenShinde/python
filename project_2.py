def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in input_string if char not in vowels)

user_input = input()
result = remove_vowels(user_input)
print( result)
