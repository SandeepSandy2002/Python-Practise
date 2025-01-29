'''
9. String Analysis Tool
   - Write a program to analyze a string:
     - Count vowels, consonants, digits, and special characters.
     - Reverse the string and display the result.
'''
word=input('enter the word')
v = s = c = n = 0
vowel = ['a','e','i','o','u']
for char in word:
  if char.isnumeric() :
    n += 1
  elif char in vowel:
    v += 1
  elif char not in vowel and char.isalpha():
    c += 1
  else:
    s += 1
print(f"vowels = {v} \n consonants = {c} \n digits = {n} \n special characters = {s}")
print(word[::-1])