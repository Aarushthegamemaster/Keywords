a = str(input("Please enter a word:"))

for i in a:
    if (i == 'a'or 'A'):
        print("A is found")
        break
    else:
        print("A was not found")
        print("Please try again")
