palindrome = input("insert a palindrome: ")

if palindrome==palindrome[::-1]:
    new_string = ""
    replaced = False
   
  for i, c in enumerate(palindrome):
        if not replaced:
            if c > 'a' and (len(palindrome)/2 != i or len(palindrome)%2 == 0):
                new_string += 'a'
                replaced = True
            else:
                new_string += c
        else:
            new_string += c
            
    if new_string == new_string[::-1]:
        print ("no way to change palindrome to non palindrome and make it lexicographically smaller")
    else:
        print ("new non palindrome lexicographically smaller string:", new_string)
else:
    print("\nenter a valid palindrome")
