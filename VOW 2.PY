def checkVowels(string):
   for char in string:
      if char in 'aeiouAEIOU':
         return True
   return False

string = input('String: ')

if (checkVowels(string) == True):
   print('Yes, String contains vowels.')
else:
   print('No, String does not contain vowels.')
