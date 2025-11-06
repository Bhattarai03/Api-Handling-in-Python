# Remove all duplicates from a list without using set().
l=[]
n=int(input("Enter a number of element you want in the string:"))
a=0
while (a!= n):
    b=int(input("Enter a element :"))
    l.append(b)
    a+=1
print(l)



newlist=[]
for item in l:
    if item not in newlist:
        newlist.append(item)
print("List without duplicate:",newlist)
