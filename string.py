chars = ['a','a','a','a','a','a','a','b','b','b','b','b','b']


letter_dict = {}
for char in chars:
    if char in letter_dict:
        letter_dict[char]+=1
        
    else:
        letter_dict[char]=1

print(letter_dict)
for i in letter_dict:
    print(letter_dict[i])

# s = ""
# value = letter_dict[char]

# for value in letter_dict:
#     if value ==1:
#         letter_dict.append(s)
#     elif value >=2:
#         letter_dict.append(s+value)
#     elif value >10:
#         letter_dict.append(s+(value/2)+s+(value/2))
#     else:
#         False

# return count(s)






