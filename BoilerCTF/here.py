
string = "079 084 108 105 077 068 089 050 077 071 078 107 079 084 086 104 090 071 086 104 077 122 073 051 089 122 085 048 077 084 103 121 089 109 070 104 078 084 069 049 079 068 081 075"


count = 0
composed_string = ""
for number in string.split(" "):
	count += 1
	int_number = int(number)
	composed_string += chr(int_number)

print("Number of Letters: ", len(string.split(" ")))
print("String decoded: ", composed_string)


