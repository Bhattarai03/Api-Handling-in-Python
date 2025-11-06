# Write a program to merge two dictionary manually.
dict1={
    "area":23,
    "length":45,
    "Breadth":56
}

dict2={
    "Volume":345,
    "Height":45,
    "Depth":456
}
dict3={}

for item in dict1:
    dict3[item]=dict1[item]
for item in dict2:
    dict3[item]=dict2[item]
print(dict3)
    