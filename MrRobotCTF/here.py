
file1 = open('fsocity.dic', 'r')
Lines = file1.readlines()


set1 = set()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    set1.add(line.strip())

print("number of lines", count)
print("number of unique lines",len(set1))
for i in set1:
   print(i)
