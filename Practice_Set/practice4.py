# Check if a string is palindrome.
a=str(input("Enter a string :"))
reverse_text=""
for char in a:
    reverse_text=char + reverse_text

if (a==reverse_text):
    print(f"The string {a} is palindrome")

else:
    print(f"The string {a} is not palindrome")