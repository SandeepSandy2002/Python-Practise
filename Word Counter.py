'''17. Word Counter
   - Create a program to count the occurrences of each word in a sentence provided by the user.
'''

statement = input("enter the statement :")
words = statement.split()
count = {}
for word in words:
  if word in count:
    count[word] += 1
  else:
    count[word] = 1
print(count)