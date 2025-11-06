# Create a list of N integers from user input.Find max,min and average.
l=[]
n=int(input("Enter a number of element you want in the string:"))
a=0
while (a!= n):
    b=int(input("Enter a element :"))
    l.append(b)
    a+=1
print(l)
sum=0
for i in range (0,n):
   
    sum=l[i]+ sum

print(f"The average of the list is {sum/n}")

max=0
for i in range(0,n):
    for j in range(1,n):
         if l[i]>l[j]:
             if l[i]>max:
               max=l[i]

         else:
           if l[j]>max:
              max=l[j]
         j+=1
    i+=1

print(f"The maximum value of element is {max}")
min=max
for i in range(0,n):
    for j in range(1,n):
         if l[i]>l[j]:
             if l[j]<min:
               min=l[j]

         else:
           if l[i]<min:
               min=l[i]
         j+=1
    i+=1
print(f"The minimum value of the list is {min}")










