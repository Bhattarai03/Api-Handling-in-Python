# Reverse  a string without slicing.

a=str(input("Enter a string :"))

reverse_text=""
for char in a:
    reverse_text=char+reverse_text

print(reverse_text)